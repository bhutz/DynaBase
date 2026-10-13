// The header selectors: problem tabs, dimension, degree, type, [K:Q] and field. The site
// is static, so every change goes to the pre-generated page for the new choice,
// data/{dimension}/{degree}/{type}/{field}/{problem}.html, where field is [K:Q] or one
// field's label. DYNABASE_NAV_DATA (assets/nav-data.js, written by generate_site.py) says
// which choices have maps: those without are marked "(no data)", and the field selector
// lists only the fields with maps on the current page.
(function () {
  var form = document.getElementById('selectors');
  if (!form) return;
  var data = window.DYNABASE_NAV_DATA || {counts: {}, fields: {}};
  var ds = form.dataset;
  var state = {dim: '1', degree: ds.degree, type: ds.type, kq: ds.kq, field: ds.field,
               problem: ds.problem || 'preper'};

  function changed(changes) {
    var s = {}, k;
    for (k in state) s[k] = state[k];
    for (k in changes) s[k] = changes[k];
    return s;
  }
  function key(s) { return s.degree + '/' + s.type + '/' + s.kq + '/' + s.problem; }
  function count(s) { return data.counts[key(s)] || 0; }
  function fields(s) { return data.fields[key(s)] || []; }
  function go(s) {
    // a field without maps for the new choice has no page: show all fields of its degree
    if (s.field && !fields(s).some(function (f) { return f[0] === s.field; })) s.field = '';
    window.location.href = ds.root + 'data/' + s.dim + '/' + s.degree + '/' + s.type + '/' +
      (s.field || s.kq) + '/' + s.problem + '.html';
  }
  function markEmpty(select, prop) {
    Array.prototype.forEach.call(select.options, function (o) {
      var c = {};
      c[prop] = o.value;
      if (!count(changed(c))) o.textContent = o.value + ' (no data)';
    });
  }

  var degree = document.getElementById('sel-degree');
  var kq = document.getElementById('sel-kq');
  var field = document.getElementById('sel-field');
  markEmpty(degree, 'degree');
  markEmpty(kq, 'kq');
  if (state.kq !== '1') {
    fields(state).forEach(function (f) {
      var o = new Option(f[1], f[0]);
      o.selected = f[0] === state.field;
      field.add(o);
    });
    field.disabled = field.options.length === 1;
  }

  degree.addEventListener('change', function () { go(changed({degree: degree.value})); });
  kq.addEventListener('change', function () { go(changed({kq: kq.value, field: ''})); });
  field.addEventListener('change', function () { go(changed({field: field.value})); });
  Array.prototype.forEach.call(document.querySelectorAll('#sel-type button'), function (b) {
    b.addEventListener('click', function () { go(changed({type: b.dataset.type})); });
  });
  Array.prototype.forEach.call(document.querySelectorAll('#problem-tabs button'), function (b) {
    b.addEventListener('click', function () { go(changed({problem: b.dataset.problem})); });
  });
  form.addEventListener('submit', function (e) { e.preventDefault(); });
})();
