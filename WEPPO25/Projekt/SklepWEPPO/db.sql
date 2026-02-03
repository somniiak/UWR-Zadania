--
-- PostgreSQL database dump
--

\restrict NEueloYk0aXdaxSRhmwXjUToFZCG0up1oUy97Qx2YLrl3Ukrh9lIGXGMrcrrEy4

-- Dumped from database version 17.6
-- Dumped by pg_dump version 17.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: order_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.order_items (
    order_id integer NOT NULL,
    product_id integer NOT NULL,
    quantity integer NOT NULL,
    price numeric(10,2) NOT NULL,
    CONSTRAINT order_items_price_check CHECK ((price >= (0)::numeric)),
    CONSTRAINT order_items_quantity_check CHECK ((quantity > 0))
);


ALTER TABLE public.order_items OWNER TO postgres;

--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    id integer NOT NULL,
    user_id integer NOT NULL,
    status text DEFAULT 'open'::text NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.orders_id_seq OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orders_id_seq OWNED BY public.orders.id;


--
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    id integer NOT NULL,
    name text NOT NULL,
    description text,
    price numeric(10,2) NOT NULL,
    CONSTRAINT products_price_check CHECK ((price >= (0)::numeric))
);


ALTER TABLE public.products OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.products_id_seq OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email text NOT NULL,
    password_hash text NOT NULL,
    role text DEFAULT 'user'::text NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: orders id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- Name: products id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: order_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.order_items (order_id, product_id, quantity, price) FROM stdin;
1	23	1	249.00
1	36	1	79.00
1	39	1	39.00
2	22	15	129.00
2	6	4	39.90
2	18	15	24.90
3	38	1	109.00
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (id, user_id, status, created_at) FROM stdin;
1	6	new	2026-02-03 00:47:17.242
2	7	new	2026-02-03 01:06:48.574
3	6	new	2026-02-03 07:41:53.362
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products (id, name, description, price) FROM stdin;
6	Podkładka pod mysz	Antypoślizgowa podkładka gamingowa	39.90
7	Lampka biurkowa LED	Lampka z regulacją jasności	89.00
8	Krzesło biurowe	Krzesło ergonomiczne z podłokietnikami	599.00
9	Biurko komputerowe	Biurko z półką na klawiaturę	499.00
10	Dysk SSD 1TB	Szybki dysk SSD NVMe	429.00
11	Powerbank 20000mAh	Powerbank z szybkim ładowaniem	159.00
12	Smartwatch	Zegarek z monitorowaniem aktywności	349.00
13	Głośnik Bluetooth	Przenośny głośnik stereo	219.00
14	Router Wi-Fi	Router Wi-Fi 6	399.00
15	Kamera internetowa	Kamera Full HD do wideorozmów	179.00
16	Torba na laptopa	Torba 15 cali z ochroną antywstrząsową	119.00
17	Plecak miejski	Plecak z przegrodą na laptopa	199.00
18	Notes A5	Notes w twardej oprawie	24.90
19	Długopis metalowy	Elegancki długopis do biura	19.90
20	Organizer na biurko	Organizer na dokumenty i akcesoria	59.00
21	Koszulka bawełniana	Koszulka unisex 100% bawełna	49.90
22	Bluza z kapturem	Bluza oversize z kieszenią	129.00
23	Kurtka przejściowa	Lekka kurtka na wiosnę i jesień	249.00
24	Spodnie jeansowe	Klasyczne jeansy slim fit	159.00
25	Koszula lniana	Koszula z lnu, długi rękaw	139.00
26	Czapka zimowa	Czapka z dzianiny	39.90
27	Szalik wełniany	Ciepły szalik z wełny	89.00
28	Skarpetki sportowe	Skarpetki oddychające (3 pary)	29.90
29	Buty sportowe	Buty do biegania	349.00
30	Pasek skórzany	Pasek ze skóry naturalnej	79.00
31	Monstera deliciosa	Roślina doniczkowa do wnętrz	99.00
32	Fikus benjamina	Popularna roślina ozdobna	89.00
33	Sansewieria	Roślina oczyszczająca powietrze	69.00
34	Sukulenty zestaw	Zestaw 3 sukulentów	59.00
35	Paproć domowa	Paproć do jasnych pomieszczeń	49.00
36	Zamiokulkas	Odporna roślina doniczkowa	79.00
37	Storczyk biały	Storczyk Phalaenopsis	89.00
38	Dracena	Roślina do salonu lub biura	109.00
39	Doniczka ceramiczna	Doniczka biała, 20 cm	39.00
40	Nawóz do roślin	Uniwersalny nawóz płynny	19.90
2	Klawiatura mechaniczna	Klawiatura mechaniczna z ledami RGB.	250.00
5	Laptop 15 cali	Laptop do pracy i nauki	3299.00
1	Słuchawki bezprzewodowe	Słuchawki Bluetooth z redukcją szumów	199.71
41	Monster Energy	Napój energetyczny	7.50
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, email, password_hash, role, created_at) FROM stdin;
1	ad6127@disroot.org	$2b$10$NoqYn0IRHdElwC9viXrtjOUmzGWlSyh3lp1l.IibGWjd3i0FeqRom	user	2026-02-02 12:37:58.108816
2	adfsd@wp.pl	$2b$10$tVZ9PQdlUfSqA0jLLl0pl.CPQP.glgSzAVoRPVWeggB33bhkOUfLC	user	2026-02-02 12:42:18.498098
3	fdsfdsfs@aaa.wp	$2b$10$kmRPEgkCcrHSrJiazWNBoO5j0zYBLb.IKjuuG7lTjT8ZsW2QMEUEa	user	2026-02-02 15:01:21.747245
4	admin@sklep.pl	$2b$10$pOy0Z9SS4hMBaKpUw5V/j.1UjKKgGmsvSHN0jWX7hMa/zJPiYRsbW	admin	2026-02-02 15:31:07.384312
5	aaadfds@wp.pl	$2b$10$YSfQttHOiGOC50q8.60zhe1Ywhd4qpstgZR/ecRXXu4nsEUxFvuqO	user	2026-02-02 16:43:46.976355
6	123@wp.pl	$2b$10$JUrbVXpsbe37bU7kpCsIbODlnDyy506g0Yilh4f.j8O1uoxq/lPgG	user	2026-02-02 23:16:28.801071
7	dsadasd@onet.pl	$2b$10$3GQ6heyR4ylmKLDJuj1dl.DCsM34cVIdB3PP5oJysMCTp4F.w.ybO	user	2026-02-03 01:04:00.741309
\.


--
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_id_seq', 3, true);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_id_seq', 43, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 7, true);


--
-- Name: order_items order_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT order_items_pkey PRIMARY KEY (order_id, product_id);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: order_items fk_order_items_order; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT fk_order_items_order FOREIGN KEY (order_id) REFERENCES public.orders(id) ON DELETE CASCADE;


--
-- Name: order_items fk_order_items_product; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_items
    ADD CONSTRAINT fk_order_items_product FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- Name: orders fk_orders_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT fk_orders_user FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

\unrestrict NEueloYk0aXdaxSRhmwXjUToFZCG0up1oUy97Qx2YLrl3Ukrh9lIGXGMrcrrEy4

