CREATE TYPE public.base_field_type AS (
	label character varying,
	degree integer
);
CREATE TYPE public.display_model_type AS ENUM (
    'original',
    'reduced',
    'monic centered',
    'chebyshev',
    'newton'
);
CREATE TYPE public.model_type AS (
	coeffs character varying[],
	resultant character varying,
	bad_primes numeric[],
	height real,
	base_field_label character varying
);
CREATE TABLE public.citations (
    label character varying NOT NULL,
    authors character varying[],
    journal character varying,
    year integer,
    citation character varying,
    mathscinet character varying,
    id integer NOT NULL
);
CREATE SEQUENCE public.citations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.citations_id_seq OWNED BY public.citations.id;
CREATE TABLE public.data_releases (
    version character varying NOT NULL,
    release_date date,
    git_commit character varying,
    sage_version character varying,
    notes text,
    summary jsonb
);
CREATE TABLE public.families_dim_1_nf (
    family_id integer NOT NULL,
    name character varying,
    degree integer,
    num_parameters integer,
    model_coeffs character varying[],
    model_resultant character varying,
    base_field_label character varying,
    base_field_degree integer,
    sigma_one character varying,
    sigma_two character varying,
    ordinal integer,
    citations integer[],
    is_polynomial boolean,
    num_critical_points integer,
    automorphism_group_cardinality integer,
    automorphism_group_iso_type character varying
);
CREATE SEQUENCE public.families_dim_1_nf_family_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.families_dim_1_nf_family_id_seq OWNED BY public.families_dim_1_nf.family_id;
CREATE TABLE public.finite_fields (
    label character varying NOT NULL,
    modulus_coeffs integer[],
    characteristic integer,
    cardinality integer
);
CREATE TABLE public.functions_dim_1_ff (
    id integer NOT NULL,
    degree integer,
    base_field_label character varying,
    base_field_degree integer,
    sigma_one character varying,
    sigma_two character varying,
    ordinal integer,
    citations integer[],
    family character varying[],
    original_model public.model_type,
    monic_centered public.model_type,
    reduced_model public.model_type,
    newton_polynomial_coeffs character varying[],
    display_model public.display_model_type,
    is_polynomial boolean,
    is_chebyshev boolean,
    is_newton boolean,
    is_lattes boolean,
    is_permutation boolean,
    automorphism_group_cardinality integer,
    rational_twists character varying[],
    rational_periodic_cycles integer[],
    rational_preperiodic_components integer[],
    avg_tail_length real
);
CREATE SEQUENCE public.functions_dim_1_ff_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.functions_dim_1_ff_id_seq OWNED BY public.functions_dim_1_ff.id;
CREATE TABLE public.functions_dim_1_nf (
    function_id integer NOT NULL,
    degree integer,
    base_field_label character varying,
    base_field_degree integer,
    sigma_one character varying,
    sigma_two character varying,
    ordinal integer,
    citations integer[],
    family integer[],
    original_model public.model_type,
    monic_centered public.model_type,
    reduced_model public.model_type,
    newton_polynomial_coeffs character varying[],
    display_model public.display_model_type,
    is_polynomial boolean,
    is_chebyshev boolean,
    is_newton boolean,
    is_lattes boolean,
    is_pcf boolean,
    cp_cardinality integer,
    cp_field_of_defn character varying,
    automorphism_group_cardinality integer,
    automorphism_group_iso_type character varying,
    rational_twists integer[],
    critical_portrait_graph_id character varying,
    smallest_height_ratio numeric,
    smallest_height_point character varying,
    smallest_height_model public.display_model_type,
    first_release character varying,
    last_changed_release character varying
);
CREATE SEQUENCE public.functions_dim_1_nf_function_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.functions_dim_1_nf_function_id_seq OWNED BY public.functions_dim_1_nf.function_id;
CREATE TABLE public.graphs_dim_1_nf (
    graph_id integer NOT NULL,
    cardinality integer,
    edges integer[],
    num_components integer,
    periodic_cycles integer[],
    periodic_cardinality integer,
    preperiodic_components integer[],
    positive_in_degree integer,
    max_tail integer,
    type integer
);
CREATE SEQUENCE public.graphs_dim_1_nf_graph_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.graphs_dim_1_nf_graph_id_seq OWNED BY public.graphs_dim_1_nf.graph_id;
CREATE TABLE public.rational_preperiodic_dim_1_nf (
    id integer NOT NULL,
    function_id integer,
    base_field_label character varying,
    rational_periodic_points character varying[],
    graph_id integer
);
CREATE SEQUENCE public.rational_preperiodic_dim_1_nf_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER SEQUENCE public.rational_preperiodic_dim_1_nf_id_seq OWNED BY public.rational_preperiodic_dim_1_nf.id;
ALTER TABLE ONLY public.citations ALTER COLUMN id SET DEFAULT nextval('public.citations_id_seq'::regclass);
ALTER TABLE ONLY public.families_dim_1_nf ALTER COLUMN family_id SET DEFAULT nextval('public.families_dim_1_nf_family_id_seq'::regclass);
ALTER TABLE ONLY public.functions_dim_1_ff ALTER COLUMN id SET DEFAULT nextval('public.functions_dim_1_ff_id_seq'::regclass);
ALTER TABLE ONLY public.functions_dim_1_nf ALTER COLUMN function_id SET DEFAULT nextval('public.functions_dim_1_nf_function_id_seq'::regclass);
ALTER TABLE ONLY public.graphs_dim_1_nf ALTER COLUMN graph_id SET DEFAULT nextval('public.graphs_dim_1_nf_graph_id_seq'::regclass);
ALTER TABLE ONLY public.rational_preperiodic_dim_1_nf ALTER COLUMN id SET DEFAULT nextval('public.rational_preperiodic_dim_1_nf_id_seq'::regclass);
ALTER TABLE ONLY public.citations
    ADD CONSTRAINT citations_pkey PRIMARY KEY (label);
ALTER TABLE ONLY public.data_releases
    ADD CONSTRAINT data_releases_pkey PRIMARY KEY (version);
ALTER TABLE ONLY public.families_dim_1_nf
    ADD CONSTRAINT families_dim_1_nf_pkey PRIMARY KEY (family_id);
ALTER TABLE ONLY public.finite_fields
    ADD CONSTRAINT finite_fields_pkey PRIMARY KEY (label);
ALTER TABLE ONLY public.functions_dim_1_ff
    ADD CONSTRAINT functions_dim_1_ff_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.functions_dim_1_nf
    ADD CONSTRAINT functions_dim_1_nf_pkey PRIMARY KEY (function_id);
ALTER TABLE ONLY public.graphs_dim_1_nf
    ADD CONSTRAINT graphs_dim_1_nf_pkey PRIMARY KEY (graph_id);
ALTER TABLE ONLY public.rational_preperiodic_dim_1_nf
    ADD CONSTRAINT rational_preperiodic_dim_1_nf_pkey PRIMARY KEY (id);
