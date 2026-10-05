"""
Images of the graph structures (graphs_dim_1_NF) for the site - graphs of rational
preperiodic points and critical portraits of PCF maps: one small SVG per graph_id,
written to docs/graphs/{graph_id}.svg and linked from the tables.

A graph's edges are stored as an array: point i maps to point edges[i]. Every
vertex has exactly one outgoing edge, so each component is a cycle with trees
hanging off it, and the layout uses that (pure Python, no Graphviz or Sage):

- the cycle is in the middle, its vertices evenly spaced on a circle, and the cycle
  edges are arcs of it (a 2-cycle is two half circles);
- each tree is a layered tree pointing straight away from the cycle: the points k
  steps from the cycle are all k*STEP out, and siblings spread sideways, so levels
  line up and branches go in a consistent direction (see _layout_component);
- a fixed point's tree hangs straight down and its loop sits on top, so no vertex
  lands inside a loop;
- components are packed in rows.

Vertices and edges are unlabeled. The SVG is written compactly (one arrowhead
marker and the styles shared through groups, one decimal), a few KB at most.
"""

import math
import os

GRAPH_DIR = 'graphs'

NODE_R = 3.5                    # vertex radius
SPACING = 22.0                  # sideways distance between neighboring leaves
STEP = 40.0                     # level-to-level distance along a tree: the length of a tree edge
MIN_CYCLE_R = 15.0              # smallest circle for a cycle of length >= 2
LOOP_R = 8.0                    # fixed point loop radius
LOOP_DIR = math.pi / 2          # loops point up
MARGIN = 8.0
COMPONENT_GAP = 26.0

NODE_COLOR = '#1b2a4a'
EDGE_COLOR = '#555'


def _cycles_and_trees(edges):
    """the cycles (each in map order) and, for every vertex, its preimages off the cycles"""
    n = len(edges)
    state = [0] * n  # 0 unseen, 1 on the current walk, 2 done
    cycles = []
    for s in range(n):
        walk, v = [], s
        while state[v] == 0:
            state[v] = 1
            walk.append(v)
            v = edges[v]
        if state[v] == 1:  # the walk closed up on itself: a new cycle
            cycles.append(walk[walk.index(v):])
        for u in walk:
            state[u] = 2
    on_cycle = {v for c in cycles for v in c}
    children = [[] for _ in range(n)]
    for u in range(n):
        if u not in on_cycle:
            children[edges[u]].append(u)
    return cycles, children


def _tree_layout(root, children):
    """
    The tree hanging off a cycle vertex, as a layered tree: {vertex: (level, offset)},
    level = steps from the cycle, offset = sideways position (leaves SPACING apart,
    a parent centered over its children), the root at offset 0. Also returns the
    tree's half-width (largest |offset|).
    """
    res, slot = {}, [0]

    def place(v, level):
        kids = children[v]
        if not kids:
            off = slot[0] * SPACING
            slot[0] += 1
        else:
            offs = [place(c, level + 1) for c in kids]
            off = (offs[0] + offs[-1]) / 2
        res[v] = (level, off)
        return off

    place(root, 0)
    shift = res[root][1]
    res = {v: (lv, off - shift) for v, (lv, off) in res.items()}
    return res, max(abs(off) for _, off in res.values())


def _cycle_radius(half_widths):
    """
    The smallest cycle radius at which neighboring trees stay SPACING apart.

    A tree points straight out from its cycle vertex, so seen from the center it
    reaches furthest sideways at its first level, at radius r0 + STEP: the angle
    atan(w / (r0 + STEP)) off its own direction, w its half-width. Further out it
    only narrows in angle. So neighbors i, i+1 (directions 2 pi / n apart) are clear
    if those two angles plus the angle SPACING subtends there fit in 2 pi / n. The
    cycle vertices themselves must also be SPACING apart. (For a 2-cycle the trees
    point in opposite directions and can never meet.)
    """
    n = len(half_widths)
    sector = 2 * math.pi / n

    def clear(r0):
        r = r0 + STEP
        return all(math.atan(half_widths[i] / r) + math.atan(half_widths[(i + 1) % n] / r) + SPACING / r <= sector
                   for i in range(n))

    lo = max(MIN_CYCLE_R, SPACING / (2 * math.sin(math.pi / n)))
    if clear(lo):
        return lo
    hi = lo
    while not clear(hi):
        hi *= 2
    for _ in range(40):  # bisect
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if clear(mid) else (mid, hi)
    return hi


def _layout_component(cycle, children):
    """
    positions {vertex: (x, y)} (y up), straight edges, cycle arcs and loop, for one component.

    The cycle is centered, its vertices evenly spaced on a circle. Each cycle vertex's
    tree is a layered tree pointing straight away from the cycle (along the radius
    through that vertex): level k is k*STEP out from the cycle, siblings spread
    perpendicular to that direction - so every level is the same distance from the
    cycle and branches always go the same way. The circle is just big enough that
    neighboring trees stay apart (_cycle_radius).
    A fixed point's tree hangs straight down, with the loop on top.
    """
    n = len(cycle)
    trees = [_tree_layout(c, children) for c in cycle]
    if n == 1:
        angles, r0 = [LOOP_DIR + math.pi], 0.0  # the tree points away from the loop
    else:
        angles = [LOOP_DIR + 2 * math.pi * i / n for i in range(n)]  # map order, counterclockwise
        r0 = _cycle_radius([t[1] for t in trees])
    pos, angle = {}, {}
    for c, a, (tree, _) in zip(cycle, angles, trees):
        ux, uy = math.cos(a), math.sin(a)  # outward
        vx, vy = -uy, ux                   # sideways
        bx, by = r0 * ux, r0 * uy
        for v, (level, off) in tree.items():
            pos[v] = (bx + level * STEP * ux + off * vx, by + level * STEP * uy + off * vy)
        angle[c] = a

    lines = [(u, p) for p in pos for u in children[p]]  # tree edges u -> p
    arcs = [] if n == 1 else [(cycle[i], cycle[(i + 1) % n], r0) for i in range(n)]
    loop = cycle[0] if n == 1 else None
    return pos, lines, arcs, loop, angle


def _fmt(v):
    s = f'{v:.1f}'
    return s[:-2] if s.endswith('.0') else s


def graph_svg(edges):
    """the SVG of the directed graph with edges i -> edges[i]"""
    cycles, children = _cycles_and_trees(edges)
    comps = []
    for cycle in cycles:
        pos, lines, arcs, loop, angle = _layout_component(cycle, children)
        xs = [x for x, _ in pos.values()]
        ys = [y for _, y in pos.values()]
        box = [min(xs) - NODE_R, min(ys) - NODE_R, max(xs) + NODE_R, max(ys) + NODE_R]
        if arcs:
            r0 = arcs[0][2]
            box = [min(box[0], -r0 - 1), min(box[1], -r0 - 1), max(box[2], r0 + 1), max(box[3], r0 + 1)]
        if loop is not None:
            cx, cy = (LOOP_R + 0.4 * NODE_R) * math.cos(LOOP_DIR), (LOOP_R + 0.4 * NODE_R) * math.sin(LOOP_DIR)
            box = [min(box[0], cx - LOOP_R - 1), min(box[1], cy - LOOP_R - 1),
                   max(box[2], cx + LOOP_R + 1), max(box[3], cy + LOOP_R + 1)]
        comps.append((pos, lines, arcs, loop, angle, box))

    # pack components in rows, biggest first
    comps.sort(key=lambda c: -(c[5][3] - c[5][1]) * (c[5][2] - c[5][0]))
    area = sum((c[5][2] - c[5][0] + COMPONENT_GAP) * (c[5][3] - c[5][1] + COMPONENT_GAP) for c in comps)
    row_width = max(max(c[5][2] - c[5][0] for c in comps), 1.3 * math.sqrt(area))
    offsets, x, y, row_h = [], 0.0, 0.0, 0.0
    for c in comps:
        w, h = c[5][2] - c[5][0], c[5][3] - c[5][1]
        if x > 0 and x + w > row_width:
            x, y, row_h = 0.0, y + row_h + COMPONENT_GAP, 0.0
        offsets.append((x - c[5][0], y + c[5][3]))  # screen y = offset - y_math (y flipped)
        x += w + COMPONENT_GAP
        row_h = max(row_h, h)
    width = max(ox + c[5][2] for (ox, _), c in zip(offsets, comps)) + 2 * MARGIN
    height = y + row_h + 2 * MARGIN

    paths, circles = [], []
    for (ox, oy), (pos, lines, arcs, loop, angle, _) in zip(offsets, comps):
        def S(p):  # math coordinates -> screen
            return ox + MARGIN + p[0], oy + MARGIN - p[1]
        for u, p in lines:
            (x1, y1), (x2, y2) = S(pos[u]), S(pos[p])
            dx, dy = x2 - x1, y2 - y1
            dist = math.hypot(dx, dy)
            ux, uy = dx / dist, dy / dist
            paths.append(f'M{_fmt(x1 + NODE_R * ux)} {_fmt(y1 + NODE_R * uy)}'
                         f'L{_fmt(x2 - (NODE_R + 0.6) * ux)} {_fmt(y2 - (NODE_R + 0.6) * uy)}')
        for u, v, r0 in arcs:
            a0, a1 = angle[u], angle[v]
            if a1 <= a0:
                a1 += 2 * math.pi
            delta = (NODE_R + 0.6) / r0
            s0, s1 = a0 + delta, a1 - delta
            p0 = S((r0 * math.cos(s0), r0 * math.sin(s0)))
            p1 = S((r0 * math.cos(s1), r0 * math.sin(s1)))
            large = 1 if s1 - s0 > math.pi else 0
            # counterclockwise in math coordinates (y up): sweep-flag 0 once y is flipped
            paths.append(f'M{_fmt(p0[0])} {_fmt(p0[1])}A{_fmt(r0)} {_fmt(r0)} 0 {large} 0 '
                         f'{_fmt(p1[0])} {_fmt(p1[1])}')
        if loop is not None:
            d = LOOP_R + 0.4 * NODE_R  # loop center's distance from the vertex
            c = (d * math.cos(LOOP_DIR), d * math.sin(LOOP_DIR))
            rho = NODE_R + 0.6  # where the loop leaves and meets the vertex
            phi = math.acos((d * d + LOOP_R * LOOP_R - rho * rho) / (2 * d * LOOP_R))
            back = LOOP_DIR + math.pi
            p0 = S((c[0] + LOOP_R * math.cos(back + phi), c[1] + LOOP_R * math.sin(back + phi)))
            p1 = S((c[0] + LOOP_R * math.cos(back - phi), c[1] + LOOP_R * math.sin(back - phi)))
            # the long way round, counterclockwise in math coordinates: sweep-flag 0 as for the arcs
            paths.append(f'M{_fmt(p0[0])} {_fmt(p0[1])}A{_fmt(LOOP_R)} {_fmt(LOOP_R)} 0 1 0 '
                         f'{_fmt(p1[0])} {_fmt(p1[1])}')
        for v in pos:
            x, y = S(pos[v])
            circles.append(f'<circle cx="{_fmt(x)}" cy="{_fmt(y)}" r="{_fmt(NODE_R)}"/>')

    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{_fmt(width)}" height="{_fmt(height)}" '
            f'viewBox="0 0 {_fmt(width)} {_fmt(height)}">'
            f'<defs><marker id="a" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="5.5" '
            f'markerHeight="5.5" orient="auto"><path d="M0 0L10 5L0 10z" fill="{EDGE_COLOR}"/></marker></defs>'
            # marker-end only marks the end of a whole path, so each edge is its own path
            f'<g fill="none" stroke="{EDGE_COLOR}" stroke-width="1.1" marker-end="url(#a)">'
            + ''.join(f'<path d="{d}"/>' for d in paths) +
            f'</g><g fill="{NODE_COLOR}">' + ''.join(circles) + '</g></svg>\n')


def write_graph_images(site_dir, graphs):
    """
    graphs: {graph_id: edges}. Writes docs/graphs/{graph_id}.svg for each and
    returns the set of graph_ids that have an image. An empty graph (no rational
    preperiodic points) gets no image, so its table cell is a dash.
    """
    os.makedirs(os.path.join(site_dir, GRAPH_DIR), exist_ok=True)
    graphs = {g: e for g, e in graphs.items() if e}
    for graph_id, edges in graphs.items():
        with open(os.path.join(site_dir, GRAPH_DIR, f'{graph_id}.svg'), 'w', encoding='utf-8') as f:
            f.write(graph_svg(edges))
    return set(graphs)


def graph_link(graph_id, root, available, title='Open the graph of the rational preperiodic points'):
    """the table cell linking to a graph's image, or a dash if it has none"""
    if graph_id is None or graph_id not in available:
        return '&mdash;'
    return (f'<a href="{root}{GRAPH_DIR}/{graph_id}.svg" target="_blank" rel="noopener" '
            f'title="{title}">view</a>')
