--
-- PostgreSQL database dump
--

-- Dumped from database version 11.2
-- Dumped by pg_dump version 11.2

-- Started on 2019-02-19 18:56:26

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 197 (class 1259 OID 16579)
-- Name: titanic; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.titanic (
    id integer NOT NULL,
    survived boolean,
    pclass integer,
    name text,
    sex_male boolean,
    age double precision,
    siblings_spouses integer,
    parents_children integer,
    fare double precision
);


ALTER TABLE public.titanic OWNER TO postgres;

--
-- TOC entry 196 (class 1259 OID 16577)
-- Name: titanic_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.titanic_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.titanic_id_seq OWNER TO postgres;

--
-- TOC entry 2817 (class 0 OID 0)
-- Dependencies: 196
-- Name: titanic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.titanic_id_seq OWNED BY public.titanic.id;


--
-- TOC entry 2686 (class 2604 OID 16582)
-- Name: titanic id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.titanic ALTER COLUMN id SET DEFAULT nextval('public.titanic_id_seq'::regclass);


--
-- TOC entry 2811 (class 0 OID 16579)
-- Dependencies: 197
-- Data for Name: titanic; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.titanic (id, survived, pclass, name, sex_male, age, siblings_spouses, parents_children, fare) FROM stdin;
1	f	3	Mr. Owen Harris Braund	t	22	1	0	7.25
2	t	1	Mrs. John Bradley (Florence Briggs Thayer) Cumings	f	38	1	0	71.283299999999997
3	t	3	Miss. Laina Heikkinen	f	26	0	0	7.92499999999999982
4	t	1	Mrs. Jacques Heath (Lily May Peel) Futrelle	f	35	1	0	53.1000000000000014
5	f	3	Mr. William Henry Allen	t	35	0	0	8.05000000000000071
6	f	3	Mr. James Moran	t	27	0	0	8.45829999999999949
7	f	1	Mr. Timothy J McCarthy	t	54	0	0	51.8624999999999972
8	f	3	Master. Gosta Leonard Palsson	t	2	3	1	21.0749999999999993
9	t	3	Mrs. Oscar W (Elisabeth Vilhelmina Berg) Johnson	f	27	0	2	11.1333000000000002
10	t	2	Mrs. Nicholas (Adele Achem) Nasser	f	14	1	0	30.0707999999999984
11	t	3	Miss. Marguerite Rut Sandstrom	f	4	1	1	16.6999999999999993
12	t	1	Miss. Elizabeth Bonnell	f	58	0	0	26.5500000000000007
13	f	3	Mr. William Henry Saundercock	t	20	0	0	8.05000000000000071
14	f	3	Mr. Anders Johan Andersson	t	39	1	5	31.2749999999999986
15	f	3	Miss. Hulda Amanda Adolfina Vestrom	f	14	0	0	7.85419999999999963
16	t	2	Mrs. (Mary D Kingcome) Hewlett	f	55	0	0	16
17	f	3	Master. Eugene Rice	t	2	4	1	29.125
18	t	2	Mr. Charles Eugene Williams	t	23	0	0	13
19	f	3	Mrs. Julius (Emelia Maria Vandemoortele) Vander Planke	f	31	1	0	18
20	t	3	Mrs. Fatima Masselmani	f	22	0	0	7.22499999999999964
21	f	2	Mr. Joseph J Fynney	t	35	0	0	26
22	t	2	Mr. Lawrence Beesley	t	34	0	0	13
23	t	3	Miss. Anna McGowan	f	15	0	0	8.02919999999999945
24	t	1	Mr. William Thompson Sloper	t	28	0	0	35.5
25	f	3	Miss. Torborg Danira Palsson	f	8	3	1	21.0749999999999993
26	t	3	Mrs. Carl Oscar (Selma Augusta Emilia Johansson) Asplund	f	38	1	5	31.3874999999999993
27	f	3	Mr. Farred Chehab Emir	t	26	0	0	7.22499999999999964
28	f	1	Mr. Charles Alexander Fortune	t	19	3	2	263
29	t	3	Miss. Ellen O'Dwyer	f	24	0	0	7.87919999999999998
30	f	3	Mr. Lalio Todoroff	t	23	0	0	7.89580000000000037
31	f	1	Don. Manuel E Uruchurtu	t	40	0	0	27.7208000000000006
32	t	1	Mrs. William Augustus (Marie Eugenie) Spencer	f	48	1	0	146.520800000000008
33	t	3	Miss. Mary Agatha Glynn	f	18	0	0	7.75
34	f	2	Mr. Edward H Wheadon	t	66	0	0	10.5
35	f	1	Mr. Edgar Joseph Meyer	t	28	1	0	82.1707999999999998
36	f	1	Mr. Alexander Oskar Holverson	t	42	1	0	52
37	t	3	Mr. Hanna Mamee	t	18	0	0	7.22919999999999963
38	f	3	Mr. Ernest Charles Cann	t	21	0	0	8.05000000000000071
39	f	3	Miss. Augusta Maria Vander Planke	f	18	2	0	18
40	t	3	Miss. Jamila Nicola-Yarred	f	14	1	0	11.2416999999999998
41	f	3	Mrs. Johan (Johanna Persdotter Larsson) Ahlin	f	40	1	0	9.47499999999999964
42	f	2	Mrs. William John Robert (Dorothy Ann Wonnacott) Turpin	f	27	1	0	21
43	t	2	Miss. Simonne Marie Anne Andree Laroche	f	3	1	2	41.5792000000000002
44	t	3	Miss. Margaret Delia Devaney	f	19	0	0	7.87919999999999998
45	f	3	Mr. William John Rogers	t	30	0	0	8.05000000000000071
46	f	3	Mr. Denis Lennon	t	20	1	0	15.5
47	t	3	Miss. Bridget O'Driscoll	f	27	0	0	7.75
48	f	3	Mr. Youssef Samaan	t	16	2	0	21.6792000000000016
49	f	3	Mrs. Josef (Josefine Franchi) Arnold-Franchi	f	18	1	0	17.8000000000000007
50	f	3	Master. Juha Niilo Panula	t	7	4	1	39.6875
51	f	3	Mr. Richard Cater Nosworthy	t	21	0	0	7.79999999999999982
52	t	1	Mrs. Henry Sleeper (Myna Haxtun) Harper	f	49	1	0	76.7292000000000058
53	t	2	Mrs. Lizzie (Elizabeth Anne Wilkinson) Faunthorpe	f	29	1	0	26
54	f	1	Mr. Engelhart Cornelius Ostby	t	65	0	1	61.9791999999999987
55	t	1	Mr. Hugh Woolner	t	46	0	0	35.5
56	t	2	Miss. Emily Rugg	f	21	0	0	10.5
57	f	3	Mr. Mansouer Novel	t	28.5	0	0	7.22919999999999963
58	t	2	Miss. Constance Mirium West	f	5	1	2	27.75
59	f	3	Master. William Frederick Goodwin	t	11	5	2	46.8999999999999986
60	f	3	Mr. Orsen Sirayanian	t	22	0	0	7.22919999999999963
61	t	1	Miss. Amelie Icard	f	38	0	0	80
62	f	1	Mr. Henry Birkhardt Harris	t	45	1	0	83.4749999999999943
63	f	3	Master. Harald Skoog	t	4	3	2	27.8999999999999986
64	f	1	Mr. Albert A Stewart	t	64	0	0	27.7208000000000006
65	t	3	Master. Gerios Moubarek	t	7	1	1	15.2457999999999991
66	t	2	Mrs. (Elizabeth Ramell) Nye	f	29	0	0	10.5
67	f	3	Mr. Ernest James Crease	t	19	0	0	8.15830000000000055
68	t	3	Miss. Erna Alexandra Andersson	f	17	4	2	7.92499999999999982
69	f	3	Mr. Vincenz Kink	t	26	2	0	8.66249999999999964
70	f	2	Mr. Stephen Curnow Jenkin	t	32	0	0	10.5
71	f	3	Miss. Lillian Amy Goodwin	f	16	5	2	46.8999999999999986
72	f	2	Mr. Ambrose Jr Hood	t	21	0	0	73.5
73	f	3	Mr. Apostolos Chronopoulos	t	26	1	0	14.4542000000000002
74	t	3	Mr. Lee Bing	t	32	0	0	56.4958000000000027
75	f	3	Mr. Sigurd Hansen Moen	t	25	0	0	7.65000000000000036
76	f	3	Mr. Ivan Staneff	t	23	0	0	7.89580000000000037
77	f	3	Mr. Rahamin Haim Moutal	t	28	0	0	8.05000000000000071
78	t	2	Master. Alden Gates Caldwell	t	0.82999999999999996	0	2	29
79	t	3	Miss. Elizabeth Dowdell	f	30	0	0	12.4749999999999996
80	f	3	Mr. Achille Waelens	t	22	0	0	9
81	t	3	Mr. Jan Baptist Sheerlinck	t	29	0	0	9.5
82	t	3	Miss. Brigdet Delia McDermott	f	31	0	0	7.78749999999999964
83	f	1	Mr. Francisco M Carrau	t	28	0	0	47.1000000000000014
84	t	2	Miss. Bertha Ilett	f	17	0	0	10.5
85	t	3	Mrs. Karl Alfred (Maria Mathilda Gustafsson) Backstrom	f	33	3	0	15.8499999999999996
86	f	3	Mr. William Neal Ford	t	16	1	3	34.375
87	f	3	Mr. Selman Francis Slocovski	t	20	0	0	8.05000000000000071
88	t	1	Miss. Mabel Helen Fortune	f	23	3	2	263
89	f	3	Mr. Francesco Celotti	t	24	0	0	8.05000000000000071
90	f	3	Mr. Emil Christmann	t	29	0	0	8.05000000000000071
91	f	3	Mr. Paul Edvin Andreasson	t	20	0	0	7.85419999999999963
92	f	1	Mr. Herbert Fuller Chaffee	t	46	1	0	61.1749999999999972
93	f	3	Mr. Bertram Frank Dean	t	26	1	2	20.5749999999999993
94	f	3	Mr. Daniel Coxon	t	59	0	0	7.25
95	f	3	Mr. Charles Joseph Shorney	t	22	0	0	8.05000000000000071
96	f	1	Mr. George B Goldschmidt	t	71	0	0	34.654200000000003
97	t	1	Mr. William Bertram Greenfield	t	23	0	1	63.3582999999999998
98	t	2	Mrs. John T (Ada Julia Bone) Doling	f	34	0	1	23
99	f	2	Mr. Sinai Kantor	t	34	1	0	26
100	f	3	Miss. Matilda Petranec	f	28	0	0	7.89580000000000037
101	f	3	Mr. Pastcho Petroff	t	29	0	0	7.89580000000000037
102	f	1	Mr. Richard Frasar White	t	21	0	1	77.2874999999999943
103	f	3	Mr. Gustaf Joel Johansson	t	33	0	0	8.65419999999999945
104	f	3	Mr. Anders Vilhelm Gustafsson	t	37	2	0	7.92499999999999982
105	f	3	Mr. Stoytcho Mionoff	t	28	0	0	7.89580000000000037
106	t	3	Miss. Anna Kristine Salkjelsvik	f	21	0	0	7.65000000000000036
107	t	3	Mr. Albert Johan Moss	t	29	0	0	7.77500000000000036
108	f	3	Mr. Tido Rekic	t	38	0	0	7.89580000000000037
109	t	3	Miss. Bertha Moran	f	28	1	0	24.1499999999999986
110	f	1	Mr. Walter Chamberlain Porter	t	47	0	0	52
111	f	3	Miss. Hileni Zabour	f	14.5	1	0	14.4542000000000002
112	f	3	Mr. David John Barton	t	22	0	0	8.05000000000000071
113	f	3	Miss. Katriina Jussila	f	20	1	0	9.82499999999999929
114	f	3	Miss. Malake Attalah	f	17	0	0	14.4582999999999995
115	f	3	Mr. Edvard Pekoniemi	t	21	0	0	7.92499999999999982
116	f	3	Mr. Patrick Connors	t	70.5	0	0	7.75
117	f	2	Mr. William John Robert Turpin	t	29	1	0	21
118	f	1	Mr. Quigg Edmond Baxter	t	24	0	1	247.520800000000008
119	f	3	Miss. Ellis Anna Maria Andersson	f	2	4	2	31.2749999999999986
120	f	2	Mr. Stanley George Hickman	t	21	2	0	73.5
121	f	3	Mr. Leonard Charles Moore	t	19	0	0	8.05000000000000071
122	f	2	Mr. Nicholas Nasser	t	32.5	1	0	30.0707999999999984
123	t	2	Miss. Susan Webber	f	32.5	0	0	13
124	f	1	Mr. Percival Wayland White	t	54	0	1	77.2874999999999943
125	t	3	Master. Elias Nicola-Yarred	t	12	1	0	11.2416999999999998
126	f	3	Mr. Martin McMahon	t	19	0	0	7.75
127	t	3	Mr. Fridtjof Arne Madsen	t	24	0	0	7.14170000000000016
128	t	3	Miss. Anna Peter	f	2	1	1	22.3582999999999998
129	f	3	Mr. Johan Ekstrom	t	45	0	0	6.97499999999999964
130	f	3	Mr. Jozef Drazenoic	t	33	0	0	7.89580000000000037
131	f	3	Mr. Domingos Fernandeo Coelho	t	20	0	0	7.04999999999999982
132	f	3	Mrs. Alexander A (Grace Charity Laury) Robins	f	47	1	0	14.5
133	t	2	Mrs. Leopold (Mathilde Francoise Pede) Weisz	f	29	1	0	26
134	f	2	Mr. Samuel James Hayden Sobey	t	25	0	0	13
135	f	2	Mr. Emile Richard	t	23	0	0	15.0457999999999998
136	t	1	Miss. Helen Monypeny Newsom	f	19	0	2	26.2833000000000006
137	f	1	Mr. Jacques Heath Futrelle	t	37	1	0	53.1000000000000014
138	f	3	Mr. Olaf Elon Osen	t	16	0	0	9.21669999999999945
139	f	1	Mr. Victor Giglio	t	24	0	0	79.2000000000000028
140	f	3	Mrs. Joseph (Sultana) Boulos	f	40	0	2	15.2457999999999991
141	t	3	Miss. Anna Sofia Nysten	f	22	0	0	7.75
142	t	3	Mrs. Pekka Pietari (Elin Matilda Dolck) Hakkarainen	f	24	1	0	15.8499999999999996
143	f	3	Mr. Jeremiah Burke	t	19	0	0	6.75
144	f	2	Mr. Edgardo Samuel Andrew	t	18	0	0	11.5
145	f	2	Mr. Joseph Charles Nicholls	t	19	1	1	36.75
146	t	3	Mr. August Edvard Andersson	t	27	0	0	7.79579999999999984
147	f	3	Miss. Robina Maggie Ford	f	9	2	2	34.375
148	f	2	Mr. Michel Navratil	t	36.5	0	2	26
149	f	2	Rev. Thomas Roussel Davids Byles	t	42	0	0	13
150	f	2	Rev. Robert James Bateman	t	51	0	0	12.5250000000000004
151	t	1	Mrs. Thomas (Edith Wearne) Pears	f	22	1	0	66.5999999999999943
152	f	3	Mr. Alfonzo Meo	t	55.5	0	0	8.05000000000000071
153	f	3	Mr. Austin Blyler van Billiard	t	40.5	0	2	14.5
154	f	3	Mr. Ole Martin Olsen	t	27	0	0	7.3125
155	f	1	Mr. Charles Duane Williams	t	51	0	1	61.3791999999999973
156	t	3	Miss. Katherine Gilnagh	f	16	0	0	7.73329999999999984
157	f	3	Mr. Harry Corn	t	30	0	0	8.05000000000000071
158	f	3	Mr. Mile Smiljanic	t	37	0	0	8.66249999999999964
159	f	3	Master. Thomas Henry Sage	t	5	8	2	69.5499999999999972
160	f	3	Mr. John Hatfield Cribb	t	44	0	1	16.1000000000000014
161	t	2	Mrs. James (Elizabeth Inglis Milne) Watt	f	40	0	0	15.75
162	f	3	Mr. John Viktor Bengtsson	t	26	0	0	7.77500000000000036
163	f	3	Mr. Jovo Calic	t	17	0	0	8.66249999999999964
164	f	3	Master. Eino Viljami Panula	t	1	4	1	39.6875
165	t	3	Master. Frank John William Goldsmith	t	9	0	2	20.5249999999999986
166	t	1	Mrs. (Edith Martha Bowerman) Chibnall	f	48	0	1	55
167	f	3	Mrs. William (Anna Bernhardina Karlsson) Skoog	f	45	1	4	27.8999999999999986
168	f	1	Mr. John D Baumann	t	60	0	0	25.9250000000000007
169	f	3	Mr. Lee Ling	t	28	0	0	56.4958000000000027
170	f	1	Mr. Wyckoff Van der hoef	t	61	0	0	33.5
171	f	3	Master. Arthur Rice	t	4	4	1	29.125
172	t	3	Miss. Eleanor Ileen Johnson	f	1	1	1	11.1333000000000002
173	f	3	Mr. Antti Wilhelm Sivola	t	21	0	0	7.92499999999999982
174	f	1	Mr. James Clinch Smith	t	56	0	0	30.6957999999999984
175	f	3	Mr. Klas Albin Klasen	t	18	1	1	7.85419999999999963
176	f	3	Master. Henry Forbes Lefebre	t	5	3	1	25.4666999999999994
177	f	1	Miss. Ann Elizabeth Isham	f	50	0	0	28.7124999999999986
178	f	2	Mr. Reginald Hale	t	30	0	0	13
179	f	3	Mr. Lionel Leonard	t	36	0	0	0
180	f	3	Miss. Constance Gladys Sage	f	8	8	2	69.5499999999999972
181	f	2	Mr. Rene Pernot	t	39	0	0	15.0500000000000007
182	f	3	Master. Clarence Gustaf Hugo Asplund	t	9	4	2	31.3874999999999993
183	t	2	Master. Richard F Becker	t	1	2	1	39
184	t	3	Miss. Luise Gretchen Kink-Heilmann	f	4	0	2	22.0249999999999986
185	f	1	Mr. Hugh Roscoe Rood	t	39	0	0	50
186	t	3	Mrs. Thomas (Johanna Godfrey) O'Brien	f	26	1	0	15.5
187	t	1	Mr. Charles Hallace Romaine	t	45	0	0	26.5500000000000007
188	f	3	Mr. John Bourke	t	40	1	1	15.5
189	f	3	Mr. Stjepan Turcin	t	36	0	0	7.89580000000000037
190	t	2	Mrs. (Rosa) Pinsky	f	32	0	0	13
191	f	2	Mr. William Carbines	t	19	0	0	13
192	t	3	Miss. Carla Christine Nielsine Andersen-Jensen	f	19	1	0	7.85419999999999963
193	t	2	Master. Michel M Navratil	t	3	1	1	26
194	t	1	Mrs. James Joseph (Margaret Tobin) Brown	f	44	0	0	27.7208000000000006
195	t	1	Miss. Elise Lurette	f	58	0	0	146.520800000000008
196	f	3	Mr. Robert Mernagh	t	28	0	0	7.75
197	f	3	Mr. Karl Siegwart Andreas Olsen	t	42	0	1	8.40419999999999945
198	t	3	Miss. Margaret Madigan	f	21	0	0	7.75
199	f	2	Miss. Henriette Yrois	f	24	0	0	13
200	f	3	Mr. Nestor Cyriel Vande Walle	t	28	0	0	9.5
201	f	3	Mr. Frederick Sage	t	17	8	2	69.5499999999999972
202	f	3	Mr. Jakob Alfred Johanson	t	34	0	0	6.49580000000000002
203	f	3	Mr. Gerious Youseff	t	45.5	0	0	7.22499999999999964
204	t	3	Mr. Gurshon Cohen	t	18	0	0	8.05000000000000071
205	f	3	Miss. Telma Matilda Strom	f	2	0	1	10.4625000000000004
206	f	3	Mr. Karl Alfred Backstrom	t	32	1	0	15.8499999999999996
207	t	3	Mr. Nassef Cassem Albimona	t	26	0	0	18.7875000000000014
208	t	3	Miss. Helen Carr	f	16	0	0	7.75
209	t	1	Mr. Henry Blank	t	40	0	0	31
210	f	3	Mr. Ahmed Ali	t	24	0	0	7.04999999999999982
211	t	2	Miss. Clear Annie Cameron	f	35	0	0	21
212	f	3	Mr. John Henry Perkin	t	22	0	0	7.25
213	f	2	Mr. Hans Kristensen Givard	t	30	0	0	13
214	f	3	Mr. Philip Kiernan	t	22	1	0	7.75
215	t	1	Miss. Madeleine Newell	f	31	1	0	113.275000000000006
216	t	3	Miss. Eliina Honkanen	f	27	0	0	7.92499999999999982
217	f	2	Mr. Sidney Samuel Jacobsohn	t	42	1	0	27
218	t	1	Miss. Albina Bazzani	f	32	0	0	76.2917000000000058
219	f	2	Mr. Walter Harris	t	30	0	0	10.5
220	t	3	Mr. Victor Francis Sunderland	t	16	0	0	8.05000000000000071
221	f	2	Mr. James H Bracken	t	27	0	0	13
222	f	3	Mr. George Henry Green	t	51	0	0	8.05000000000000071
223	f	3	Mr. Christo Nenkoff	t	22	0	0	7.89580000000000037
224	t	1	Mr. Frederick Maxfield Hoyt	t	38	1	0	90
225	f	3	Mr. Karl Ivar Sven Berglund	t	22	0	0	9.34999999999999964
226	t	2	Mr. William John Mellors	t	19	0	0	10.5
227	f	3	Mr. John Hall Lovell	t	20.5	0	0	7.25
228	f	2	Mr. Arne Jonas Fahlstrom	t	18	0	0	13
229	f	3	Miss. Mathilde Lefebre	f	12	3	1	25.4666999999999994
230	t	1	Mrs. Henry Birkhardt (Irene Wallach) Harris	f	35	1	0	83.4749999999999943
231	f	3	Mr. Bengt Edvin Larsson	t	29	0	0	7.77500000000000036
232	f	2	Mr. Ernst Adolf Sjostedt	t	59	0	0	13.5
233	t	3	Miss. Lillian Gertrud Asplund	f	5	4	2	31.3874999999999993
234	f	2	Mr. Robert William Norman Leyson	t	24	0	0	10.5
235	f	3	Miss. Alice Phoebe Harknett	f	21	0	0	7.54999999999999982
236	f	2	Mr. Stephen Hold	t	44	1	0	26
237	t	2	Miss. Marjorie Collyer	f	8	0	2	26.25
238	f	2	Mr. Frederick William Pengelly	t	19	0	0	10.5
239	f	2	Mr. George Henry Hunt	t	33	0	0	12.2750000000000004
240	f	3	Miss. Thamine Zabour	f	19	1	0	14.4542000000000002
241	t	3	Miss. Katherine Murphy	f	18	1	0	15.5
242	f	2	Mr. Reginald Charles Coleridge	t	29	0	0	10.5
243	f	3	Mr. Matti Alexanteri Maenpaa	t	22	0	0	7.125
244	f	3	Mr. Sleiman Attalah	t	30	0	0	7.22499999999999964
245	f	1	Dr. William Edward Minahan	t	44	2	0	90
246	f	3	Miss. Agda Thorilda Viktoria Lindahl	f	25	0	0	7.77500000000000036
247	t	2	Mrs. William (Anna) Hamalainen	f	24	0	2	14.5
248	t	1	Mr. Richard Leonard Beckwith	t	37	1	1	52.5542000000000016
249	f	2	Rev. Ernest Courtenay Carter	t	54	1	0	26
250	f	3	Mr. James George Reed	t	18	0	0	7.25
251	f	3	Mrs. Wilhelm (Elna Matilda Persson) Strom	f	29	1	1	10.4625000000000004
252	f	1	Mr. William Thomas Stead	t	62	0	0	26.5500000000000007
253	f	3	Mr. William Arthur Lobb	t	30	1	0	16.1000000000000014
254	f	3	Mrs. Viktor (Helena Wilhelmina) Rosblom	f	41	0	2	20.2124999999999986
255	t	3	Mrs. Darwis (Hanne Youssef Razi) Touma	f	29	0	2	15.2457999999999991
256	t	1	Mrs. Gertrude Maybelle Thorne	f	38	0	0	79.2000000000000028
257	t	1	Miss. Gladys Cherry	f	30	0	0	86.5
258	t	1	Miss. Anna Ward	f	35	0	0	512.329200000000014
259	t	2	Mrs. (Lutie Davis) Parrish	f	50	0	1	26
260	t	3	Master. Edvin Rojj Felix Asplund	t	3	4	2	31.3874999999999993
261	f	1	Mr. Emil Taussig	t	52	1	1	79.6500000000000057
262	f	1	Mr. William Harrison	t	40	0	0	0
263	f	3	Miss. Delia Henry	f	21	0	0	7.75
264	f	2	Mr. David Reeves	t	36	0	0	10.5
265	f	3	Mr. Ernesti Arvid Panula	t	16	4	1	39.6875
266	t	3	Mr. Ernst Ulrik Persson	t	25	1	0	7.77500000000000036
267	t	1	Mrs. William Thompson (Edith Junkins) Graham	f	58	0	1	153.462500000000006
268	t	1	Miss. Amelia Bissette	f	35	0	0	135.633299999999991
269	f	1	Mr. Alexander Cairns	t	28	0	0	31
270	t	3	Mr. William Henry Tornquist	t	25	0	0	0
271	t	2	Mrs. (Elizabeth Anne Maidment) Mellinger	f	41	0	1	19.5
272	f	1	Mr. Charles H Natsch	t	37	0	1	29.6999999999999993
273	t	3	Miss. Hanora Healy	f	33	0	0	7.75
274	t	1	Miss. Kornelia Theodosia Andrews	f	63	1	0	77.9582999999999942
275	f	3	Miss. Augusta Charlotta Lindblom	f	45	0	0	7.75
276	f	2	Mr. Francis Parkes	t	21	0	0	0
277	f	3	Master. Eric Rice	t	7	4	1	29.125
278	t	3	Mrs. Stanton (Rosa Hunt) Abbott	f	35	1	1	20.25
279	f	3	Mr. Frank Duane	t	65	0	0	7.75
280	f	3	Mr. Nils Johan Goransson Olsson	t	28	0	0	7.85419999999999963
281	f	3	Mr. Alfons de Pelsmaeker	t	16	0	0	9.5
282	t	3	Mr. Edward Arthur Dorking	t	19	0	0	8.05000000000000071
283	f	1	Mr. Richard William Smith	t	57	0	0	26
284	f	3	Mr. Ivan Stankovic	t	33	0	0	8.66249999999999964
285	t	3	Mr. Theodore de Mulder	t	30	0	0	9.5
286	f	3	Mr. Penko Naidenoff	t	22	0	0	7.89580000000000037
287	t	2	Mr. Masabumi Hosono	t	42	0	0	13
288	t	3	Miss. Kate Connolly	f	22	0	0	7.75
289	t	1	Miss. Ellen Barber	f	26	0	0	78.8499999999999943
290	t	1	Mrs. Dickinson H (Helen Walton) Bishop	f	19	1	0	91.0792000000000002
291	f	2	Mr. Rene Jacques Levy	t	36	0	0	12.875
292	f	3	Miss. Aloisia Haas	f	24	0	0	8.84999999999999964
293	f	3	Mr. Ivan Mineff	t	24	0	0	7.89580000000000037
294	f	1	Mr. Ervin G Lewy	t	30	0	0	27.7208000000000006
295	f	3	Mr. Mansour Hanna	t	23.5	0	0	7.22919999999999963
296	f	1	Miss. Helen Loraine Allison	f	2	1	2	151.550000000000011
297	t	1	Mr. Adolphe Saalfeld	t	47	0	0	30.5
298	t	1	Mrs. James (Helene DeLaudeniere Chaput) Baxter	f	50	0	1	247.520800000000008
299	t	3	Miss. Anna Katherine Kelly	f	20	0	0	7.75
300	t	3	Mr. Bernard McCoy	t	24	2	0	23.25
301	f	3	Mr. William Cahoone Jr Johnson	t	19	0	0	0
302	t	2	Miss. Nora A Keane	f	46	0	0	12.3499999999999996
303	f	3	Mr. Howard Hugh Williams	t	28	0	0	8.05000000000000071
304	t	1	Master. Hudson Trevor Allison	t	0.92000000000000004	1	2	151.550000000000011
305	t	1	Miss. Margaret Fleming	f	42	0	0	110.883300000000006
306	t	1	Mrs. Victor de Satode (Maria Josefa Perez de Soto y Vallejo) Penasco y Castellana	f	17	1	0	108.900000000000006
307	f	2	Mr. Samuel Abelson	t	30	1	0	24
308	t	1	Miss. Laura Mabel Francatelli	f	30	0	0	56.9292000000000016
309	t	1	Miss. Margaret Bechstein Hays	f	24	0	0	83.158299999999997
310	t	1	Miss. Emily Borie Ryerson	f	18	2	2	262.375
311	f	2	Mrs. William (Anna Sylfven) Lahtinen	f	26	1	1	26
312	f	3	Mr. Ignjac Hendekovic	t	28	0	0	7.89580000000000037
313	f	2	Mr. Benjamin Hart	t	43	1	1	26.25
314	t	3	Miss. Helmina Josefina Nilsson	f	26	0	0	7.85419999999999963
315	t	2	Mrs. Sinai (Miriam Sternin) Kantor	f	24	1	0	26
316	f	2	Dr. Ernest Moraweck	t	54	0	0	14
317	t	1	Miss. Mary Natalie Wick	f	31	0	2	164.866700000000009
318	t	1	Mrs. Frederic Oakley (Margaretta Corning Stone) Spedden	f	40	1	1	134.5
319	f	3	Mr. Samuel Dennis	t	22	0	0	7.25
320	f	3	Mr. Yoto Danoff	t	27	0	0	7.89580000000000037
321	t	2	Miss. Hilda Mary Slayter	f	30	0	0	12.3499999999999996
322	t	2	Mrs. Albert Francis (Sylvia Mae Harbaugh) Caldwell	f	22	1	1	29
323	f	3	Mr. George John Jr Sage	t	20	8	2	69.5499999999999972
324	t	1	Miss. Marie Grice Young	f	36	0	0	135.633299999999991
325	f	3	Mr. Johan Hansen Nysveen	t	61	0	0	6.23749999999999982
326	t	2	Mrs. (Ada E Hall) Ball	f	36	0	0	13
327	t	3	Mrs. Frank John (Emily Alice Brown) Goldsmith	f	31	1	1	20.5249999999999986
328	t	1	Miss. Jean Gertrude Hippach	f	16	0	1	57.9791999999999987
329	t	3	Miss. Agnes McCoy	f	28	2	0	23.25
330	f	1	Mr. Austen Partner	t	45.5	0	0	28.5
331	f	1	Mr. George Edward Graham	t	38	0	1	153.462500000000006
332	f	3	Mr. Leo Edmondus Vander Planke	t	16	2	0	18
333	t	1	Mrs. Henry William (Clara Heinsheimer) Frauenthal	f	42	1	0	133.650000000000006
334	f	3	Mr. Mitto Denkoff	t	30	0	0	7.89580000000000037
335	f	1	Mr. Thomas Clinton Pears	t	29	1	0	66.5999999999999943
336	t	1	Miss. Elizabeth Margaret Burns	f	41	0	0	134.5
337	t	3	Mr. Karl Edwart Dahl	t	45	0	0	8.05000000000000071
338	f	1	Mr. Stephen Weart Blackwell	t	45	0	0	35.5
339	t	2	Master. Edmond Roger Navratil	t	2	1	1	26
340	t	1	Miss. Alice Elizabeth Fortune	f	24	3	2	263
341	f	2	Mr. Erik Gustaf Collander	t	28	0	0	13
342	f	2	Mr. Charles Frederick Waddington Sedgwick	t	25	0	0	13
343	f	2	Mr. Stanley Hubert Fox	t	36	0	0	13
344	t	2	Miss. Amelia Brown	f	24	0	0	13
345	t	2	Miss. Marion Elsie Smith	f	40	0	0	13
346	t	3	Mrs. Thomas Henry (Mary E Finck) Davison	f	34	1	0	16.1000000000000014
347	t	3	Master. William Loch Coutts	t	3	1	1	15.9000000000000004
348	f	3	Mr. Jovan Dimic	t	42	0	0	8.66249999999999964
349	f	3	Mr. Nils Martin Odahl	t	23	0	0	9.22499999999999964
350	f	1	Mr. Fletcher Fellows Williams-Lambert	t	43	0	0	35
351	f	3	Mr. Tannous Elias	t	15	1	1	7.22919999999999963
352	f	3	Mr. Josef Arnold-Franchi	t	25	1	0	17.8000000000000007
353	f	3	Mr. Wazli Yousif	t	23	0	0	7.22499999999999964
354	f	3	Mr. Leo Peter Vanden Steen	t	28	0	0	9.5
355	t	1	Miss. Elsie Edith Bowerman	f	22	0	1	55
356	f	2	Miss. Annie Clemmer Funk	f	38	0	0	13
357	t	3	Miss. Mary McGovern	f	22	0	0	7.87919999999999998
358	t	3	Miss. Helen Mary Mockler	f	23	0	0	7.87919999999999998
359	f	3	Mr. Wilhelm Skoog	t	40	1	4	27.8999999999999986
360	f	2	Mr. Sebastiano del Carlo	t	29	1	0	27.7208000000000006
361	f	3	Mrs. (Catherine David) Barbara	f	45	0	1	14.4542000000000002
362	f	3	Mr. Adola Asim	t	35	0	0	7.04999999999999982
363	f	3	Mr. Thomas O'Brien	t	27	1	0	15.5
364	f	3	Mr. Mauritz Nils Martin Adahl	t	30	0	0	7.25
365	t	1	Mrs. Frank Manley (Anna Sophia Atkinson) Warren	f	60	1	0	75.25
366	t	3	Mrs. (Mantoura Boulos) Moussa	f	35	0	0	7.22919999999999963
367	t	3	Miss. Annie Jermyn	f	22	0	0	7.75
368	t	1	Mme. Leontine Pauline Aubart	f	24	0	0	69.2999999999999972
369	t	1	Mr. George Achilles Harder	t	25	1	0	55.4416999999999973
370	f	3	Mr. Jakob Alfred Wiklund	t	18	1	0	6.49580000000000002
371	f	3	Mr. William Thomas Beavan	t	19	0	0	8.05000000000000071
372	f	1	Mr. Sante Ringhini	t	22	0	0	135.633299999999991
373	f	3	Miss. Stina Viola Palsson	f	3	3	1	21.0749999999999993
374	t	1	Mrs. Edgar Joseph (Leila Saks) Meyer	f	25	1	0	82.1707999999999998
375	t	3	Miss. Aurora Adelia Landergren	f	22	0	0	7.25
376	f	1	Mr. Harry Elkins Widener	t	27	0	2	211.5
377	f	3	Mr. Tannous Betros	t	20	0	0	4.01250000000000018
378	f	3	Mr. Karl Gideon Gustafsson	t	19	0	0	7.77500000000000036
379	t	1	Miss. Rosalie Bidois	f	42	0	0	227.525000000000006
380	t	3	Miss. Maria Nakid	f	1	0	2	15.7416999999999998
381	f	3	Mr. Juho Tikkanen	t	32	0	0	7.92499999999999982
382	t	1	Mrs. Alexander Oskar (Mary Aline Towner) Holverson	f	35	1	0	52
383	f	3	Mr. Vasil Plotcharsky	t	27	0	0	7.89580000000000037
384	f	2	Mr. Charles Henry Davies	t	18	0	0	73.5
385	f	3	Master. Sidney Leonard Goodwin	t	1	5	2	46.8999999999999986
386	t	2	Miss. Kate Buss	f	36	0	0	13
387	f	3	Mr. Matthew Sadlier	t	19	0	0	7.72919999999999963
388	t	2	Miss. Bertha Lehmann	f	17	0	0	12
389	t	1	Mr. William Ernest Carter	t	36	1	2	120
390	t	3	Mr. Carl Olof Jansson	t	21	0	0	7.79579999999999984
391	f	3	Mr. Johan Birger Gustafsson	t	28	2	0	7.92499999999999982
392	t	1	Miss. Marjorie Newell	f	23	1	0	113.275000000000006
393	t	3	Mrs. Hjalmar (Agnes Charlotta Bengtsson) Sandstrom	f	24	0	2	16.6999999999999993
394	f	3	Mr. Erik Johansson	t	22	0	0	7.79579999999999984
395	f	3	Miss. Elina Olsson	f	31	0	0	7.85419999999999963
396	f	2	Mr. Peter David McKane	t	46	0	0	26
397	f	2	Dr. Alfred Pain	t	23	0	0	10.5
398	t	2	Mrs. William H (Jessie L) Trout	f	28	0	0	12.6500000000000004
399	t	3	Mr. Juha Niskanen	t	39	0	0	7.92499999999999982
400	f	3	Mr. John Adams	t	26	0	0	8.05000000000000071
401	f	3	Miss. Mari Aina Jussila	f	21	1	0	9.82499999999999929
402	f	3	Mr. Pekka Pietari Hakkarainen	t	28	1	0	15.8499999999999996
403	f	3	Miss. Marija Oreskovic	f	20	0	0	8.66249999999999964
404	f	2	Mr. Shadrach Gale	t	34	1	0	21
405	f	3	Mr. Carl/Charles Peter Widegren	t	51	0	0	7.75
406	t	2	Master. William Rowe Richards	t	3	1	1	18.75
407	f	3	Mr. Hans Martin Monsen Birkeland	t	21	0	0	7.77500000000000036
408	f	3	Miss. Ida Lefebre	f	3	3	1	25.4666999999999994
409	f	3	Mr. Todor Sdycoff	t	42	0	0	7.89580000000000037
410	f	3	Mr. Henry Hart	t	27	0	0	6.85829999999999984
411	t	1	Miss. Daisy E Minahan	f	33	1	0	90
412	f	2	Mr. Alfred Fleming Cunningham	t	22	0	0	0
413	t	3	Mr. Johan Julian Sundman	t	44	0	0	7.92499999999999982
414	f	3	Mrs. Thomas (Annie Louise Rowley) Meek	f	32	0	0	8.05000000000000071
415	t	2	Mrs. James Vivian (Lulu Thorne Christian) Drew	f	34	1	1	32.5
416	t	2	Miss. Lyyli Karoliina Silven	f	18	0	2	13
417	f	2	Mr. William John Matthews	t	30	0	0	13
418	f	3	Miss. Catharina Van Impe	f	10	0	2	24.1499999999999986
419	f	3	Mr. David Charters	t	21	0	0	7.73329999999999984
420	f	3	Mr. Leo Zimmerman	t	29	0	0	7.875
421	f	3	Mrs. Ernst Gilbert (Anna Sigrid Maria Brogren) Danbom	f	28	1	1	14.4000000000000004
422	f	3	Mr. Viktor Richard Rosblom	t	18	1	1	20.2124999999999986
423	f	3	Mr. Phillippe Wiseman	t	54	0	0	7.25
424	t	2	Mrs. Charles V (Ada Maria Winfield) Clarke	f	28	1	0	26
425	t	2	Miss. Kate Florence Phillips	f	19	0	0	26
426	f	3	Mr. James Flynn	t	28	0	0	7.75
427	t	3	Mr. Berk (Berk Trembisky) Pickard	t	32	0	0	8.05000000000000071
428	t	1	Mr. Mauritz Hakan Bjornstrom-Steffansson	t	28	0	0	26.5500000000000007
429	t	3	Mrs. Percival (Florence Kate White) Thorneycroft	f	33	1	0	16.1000000000000014
430	t	2	Mrs. Charles Alexander (Alice Adelaide Slow) Louch	f	42	1	0	26
431	f	3	Mr. Nikolai Erland Kallio	t	17	0	0	7.125
432	f	1	Mr. William Baird Silvey	t	50	1	0	55.8999999999999986
433	t	1	Miss. Lucile Polk Carter	f	14	1	2	120
434	f	3	Miss. Doolina Margaret Ford	f	21	2	2	34.375
435	t	2	Mrs. Sidney (Emily Hocking) Richards	f	24	2	3	18.75
436	f	1	Mr. Mark Fortune	t	64	1	4	263
437	f	2	Mr. Johan Henrik Johannesson Kvillner	t	31	0	0	10.5
438	t	2	Mrs. Benjamin (Esther Ada Bloomfield) Hart	f	45	1	1	26.25
439	f	3	Mr. Leon Hampe	t	20	0	0	9.5
440	f	3	Mr. Johan Emil Petterson	t	25	1	0	7.77500000000000036
441	t	2	Ms. Encarnacion Reynaldo	f	28	0	0	13
442	t	3	Mr. Bernt Johannesen-Bratthammer	t	29	0	0	8.11250000000000071
443	t	1	Master. Washington Dodge	t	4	0	2	81.8582999999999998
444	t	2	Miss. Madeleine Violet Mellinger	f	13	0	1	19.5
445	t	1	Mr. Frederic Kimber Seward	t	34	0	0	26.5500000000000007
446	t	3	Miss. Marie Catherine Baclini	f	5	2	1	19.2582999999999984
447	t	1	Major. Arthur Godfrey Peuchen	t	52	0	0	30.5
448	f	2	Mr. Edwy Arthur West	t	36	1	2	27.75
449	f	3	Mr. Ingvald Olai Olsen Hagland	t	28	1	0	19.9666999999999994
450	f	1	Mr. Benjamin Laventall Foreman	t	30	0	0	27.75
451	t	1	Mr. Samuel L Goldenberg	t	49	1	0	89.1042000000000058
452	f	3	Mr. Joseph Peduzzi	t	24	0	0	8.05000000000000071
453	t	3	Mr. Ivan Jalsevac	t	29	0	0	7.89580000000000037
454	f	1	Mr. Francis Davis Millet	t	65	0	0	26.5500000000000007
455	t	1	Mrs. Frederick R (Marion) Kenyon	f	41	1	0	51.8624999999999972
456	t	2	Miss. Ellen Toomey	f	50	0	0	10.5
457	f	3	Mr. Maurice O'Connor	t	17	0	0	7.75
458	t	1	Mr. Harry Anderson	t	48	0	0	26.5500000000000007
459	f	3	Mr. William Morley	t	34	0	0	8.05000000000000071
460	f	1	Mr. Arthur H Gee	t	47	0	0	38.5
461	f	2	Mr. Jacob Christian Milling	t	48	0	0	13
462	f	3	Mr. Simon Maisner	t	34	0	0	8.05000000000000071
463	f	3	Mr. Manuel Estanslas Goncalves	t	38	0	0	7.04999999999999982
464	f	2	Mr. William Campbell	t	21	0	0	0
465	f	1	Mr. John Montgomery Smart	t	56	0	0	26.5500000000000007
466	f	3	Mr. James Scanlan	t	22	0	0	7.72499999999999964
467	t	3	Miss. Helene Barbara Baclini	f	0.75	2	1	19.2582999999999984
468	f	3	Mr. Arthur Keefe	t	39	0	0	7.25
469	f	3	Mr. Luka Cacic	t	38	0	0	8.66249999999999964
470	t	2	Mrs. Edwy Arthur (Ada Mary Worth) West	f	33	1	2	27.75
471	t	2	Mrs. Amin S (Marie Marthe Thuillard) Jerwan	f	23	0	0	13.7917000000000005
472	f	3	Miss. Ida Sofia Strandberg	f	22	0	0	9.83750000000000036
473	f	1	Mr. George Quincy Clifford	t	40	0	0	52
474	f	2	Mr. Peter Henry Renouf	t	34	1	0	21
475	f	3	Mr. Lewis Richard Braund	t	29	1	0	7.04579999999999984
476	f	3	Mr. Nils August Karlsson	t	22	0	0	7.52080000000000037
477	t	3	Miss. Hildur E Hirvonen	f	2	0	1	12.2874999999999996
478	f	3	Master. Harold Victor Goodwin	t	9	5	2	46.8999999999999986
479	f	2	Mr. Anthony Wood Frost	t	37	0	0	0
480	f	3	Mr. Richard Henry Rouse	t	50	0	0	8.05000000000000071
481	t	3	Mrs. (Hedwig) Turkula	f	63	0	0	9.58750000000000036
482	t	1	Mr. Dickinson H Bishop	t	25	1	0	91.0792000000000002
483	f	3	Miss. Jeannie Lefebre	f	8	3	1	25.4666999999999994
484	t	1	Mrs. Frederick Maxfield (Jane Anne Forby) Hoyt	f	35	1	0	90
485	f	1	Mr. Edward Austin Kent	t	58	0	0	29.6999999999999993
486	f	3	Mr. Francis William Somerton	t	30	0	0	8.05000000000000071
487	t	3	Master. Eden Leslie Coutts	t	9	1	1	15.9000000000000004
488	f	3	Mr. Konrad Mathias Reiersen Hagland	t	19	1	0	19.9666999999999994
489	f	3	Mr. Einar Windelov	t	21	0	0	7.25
490	f	1	Mr. Harry Markland Molson	t	55	0	0	30.5
491	f	1	Mr. Ramon Artagaveytia	t	71	0	0	49.5041999999999973
492	f	3	Mr. Edward Roland Stanley	t	21	0	0	8.05000000000000071
493	f	3	Mr. Gerious Yousseff	t	26	0	0	14.4582999999999995
494	t	1	Miss. Elizabeth Mussey Eustis	f	54	1	0	78.2667000000000002
495	f	3	Mr. Frederick William Shellard	t	55	0	0	15.0999999999999996
496	f	1	Mrs. Hudson J C (Bessie Waldo Daniels) Allison	f	25	1	2	151.550000000000011
497	f	3	Mr. Olof Svensson	t	24	0	0	7.79579999999999984
498	f	3	Mr. Petar Calic	t	17	0	0	8.66249999999999964
499	f	3	Miss. Mary Canavan	f	21	0	0	7.75
500	f	3	Miss. Bridget Mary O'Sullivan	f	21	0	0	7.62919999999999998
501	f	3	Miss. Kristina Sofia Laitinen	f	37	0	0	9.58750000000000036
502	t	1	Miss. Roberta Maioni	f	16	0	0	86.5
503	f	1	Mr. Victor de Satode Penasco y Castellana	t	18	1	0	108.900000000000006
504	t	2	Mrs. Frederick Charles (Jane Richards) Quick	f	33	0	2	26
505	t	1	Mr. George Bradley	t	37	0	0	26.5500000000000007
506	f	3	Mr. Henry Margido Olsen	t	28	0	0	22.5249999999999986
507	t	3	Mr. Fang Lang	t	26	0	0	56.4958000000000027
508	t	3	Mr. Eugene Patrick Daly	t	29	0	0	7.75
509	f	3	Mr. James Webber	t	66	0	0	8.05000000000000071
510	t	1	Mr. James Robert McGough	t	36	0	0	26.2875000000000014
511	t	1	Mrs. Martin (Elizabeth L. Barrett) Rothschild	f	54	1	0	59.3999999999999986
512	f	3	Mr. Satio Coleff	t	24	0	0	7.49580000000000002
513	f	1	Mr. William Anderson Walker	t	47	0	0	34.0208000000000013
514	t	2	Mrs. (Amelia Milley) Lemore	f	34	0	0	10.5
515	f	3	Mr. Patrick Ryan	t	30	0	0	24.1499999999999986
516	t	2	Mrs. William A (Florence Agnes Hughes) Angle	f	36	1	0	26
517	f	3	Mr. Stefo Pavlovic	t	32	0	0	7.89580000000000037
518	t	1	Miss. Anne Perreault	f	30	0	0	93.5
519	f	3	Mr. Janko Vovk	t	22	0	0	7.89580000000000037
520	f	3	Mr. Sarkis Lahoud	t	35	0	0	7.22499999999999964
521	t	1	Mrs. Louis Albert (Ida Sophia Fischer) Hippach	f	44	0	1	57.9791999999999987
522	f	3	Mr. Fared Kassem	t	18	0	0	7.22919999999999963
523	f	3	Mr. James Farrell	t	40.5	0	0	7.75
524	t	2	Miss. Lucy Ridsdale	f	50	0	0	10.5
525	f	1	Mr. John Farthing	t	49	0	0	221.779200000000003
526	f	3	Mr. Johan Werner Salonen	t	39	0	0	7.92499999999999982
527	f	2	Mr. Richard George Hocking	t	23	2	1	11.5
528	t	2	Miss. Phyllis May Quick	f	2	1	1	26
529	f	3	Mr. Nakli Toufik	t	17	0	0	7.22919999999999963
530	f	3	Mr. Joseph Jr Elias	t	17	1	1	7.22919999999999963
531	t	3	Mrs. Catherine (Catherine Rizk) Peter	f	24	0	2	22.3582999999999998
532	f	3	Miss. Marija Cacic	f	30	0	0	8.66249999999999964
533	t	2	Miss. Eva Miriam Hart	f	7	0	2	26.25
534	f	1	Major. Archibald Willingham Butt	t	45	0	0	26.5500000000000007
535	t	1	Miss. Bertha LeRoy	f	30	0	0	106.424999999999997
536	f	3	Mr. Samuel Beard Risien	t	69	0	0	14.5
537	t	1	Miss. Hedwig Margaritha Frolicher	f	22	0	2	49.5
538	t	1	Miss. Harriet R Crosby	f	36	0	2	71
539	f	3	Miss. Ingeborg Constanzia Andersson	f	9	4	2	31.2749999999999986
540	f	3	Miss. Sigrid Elisabeth Andersson	f	11	4	2	31.2749999999999986
541	t	2	Mr. Edward Beane	t	32	1	0	26
542	f	1	Mr. Walter Donald Douglas	t	50	1	0	106.424999999999997
543	f	1	Mr. Arthur Ernest Nicholson	t	64	0	0	26
544	t	2	Mrs. Edward (Ethel Clarke) Beane	f	19	1	0	26
545	t	2	Mr. Julian Padro y Manent	t	27	0	0	13.8625000000000007
546	f	3	Mr. Frank John Goldsmith	t	33	1	1	20.5249999999999986
547	t	2	Master. John Morgan Jr Davies	t	8	1	1	36.75
548	t	1	Mr. John Borland Jr Thayer	t	17	0	2	110.883300000000006
549	f	2	Mr. Percival James R Sharp	t	27	0	0	26
550	f	3	Mr. Timothy O'Brien	t	21	0	0	7.82920000000000016
551	t	3	Mr. Fahim Leeni	t	22	0	0	7.22499999999999964
552	t	3	Miss. Velin Ohman	f	22	0	0	7.77500000000000036
553	f	1	Mr. George Wright	t	62	0	0	26.5500000000000007
554	t	1	Lady. (Lucille Christiana Sutherland)Duff Gordon	f	48	1	0	39.6000000000000014
555	f	1	Mr. Victor Robbins	t	45	0	0	227.525000000000006
556	t	1	Mrs. Emil (Tillie Mandelbaum) Taussig	f	39	1	1	79.6500000000000057
557	t	3	Mrs. Guillaume Joseph (Emma) de Messemaeker	f	36	1	0	17.3999999999999986
558	f	3	Mr. Thomas Rowan Morrow	t	30	0	0	7.75
559	f	3	Mr. Husein Sivic	t	40	0	0	7.89580000000000037
560	f	2	Mr. Robert Douglas Norman	t	28	0	0	13.5
561	f	3	Mr. John Simmons	t	40	0	0	8.05000000000000071
562	f	3	Miss. (Marion Ogden) Meanwell	f	62	0	0	8.05000000000000071
563	f	3	Mr. Alfred J Davies	t	24	2	0	24.1499999999999986
564	f	3	Mr. Ilia Stoytcheff	t	19	0	0	7.89580000000000037
565	f	3	Mrs. Nils (Alma Cornelia Berglund) Palsson	f	29	0	4	21.0749999999999993
566	f	3	Mr. Tannous Doharr	t	28	0	0	7.22919999999999963
567	t	3	Mr. Carl Jonsson	t	32	0	0	7.85419999999999963
568	t	2	Mr. George Harris	t	62	0	0	10.5
569	t	1	Mrs. Edward Dale (Charlotte Lamson) Appleton	f	53	2	0	51.4791999999999987
570	t	1	Mr. John Irwin Flynn	t	36	0	0	26.3874999999999993
571	t	3	Miss. Mary Kelly	f	22	0	0	7.75
572	f	3	Mr. Alfred George John Rush	t	16	0	0	8.05000000000000071
573	f	3	Mr. George Patchett	t	19	0	0	14.5
574	t	2	Miss. Ethel Garside	f	34	0	0	13
575	t	1	Mrs. William Baird (Alice Munger) Silvey	f	39	1	0	55.8999999999999986
576	f	3	Mrs. Joseph (Maria Elias) Caram	f	18	1	0	14.4582999999999995
577	t	3	Mr. Eiriik Jussila	t	32	0	0	7.92499999999999982
578	t	2	Miss. Julie Rachel Christy	f	25	1	1	30
579	t	1	Mrs. John Borland (Marian Longstreth Morris) Thayer	f	39	1	1	110.883300000000006
580	f	2	Mr. William James Downton	t	54	0	0	26
581	f	1	Mr. John Hugo Ross	t	36	0	0	40.125
582	f	3	Mr. Uscher Paulner	t	16	0	0	8.71250000000000036
583	t	1	Miss. Ruth Taussig	f	18	0	2	79.6500000000000057
584	f	2	Mr. John Denzil Jarvis	t	47	0	0	15
585	t	1	Mr. Maxmillian Frolicher-Stehli	t	60	1	1	79.2000000000000028
586	f	3	Mr. Eliezer Gilinski	t	22	0	0	8.05000000000000071
587	f	3	Mr. Joseph Murdlin	t	22	0	0	8.05000000000000071
588	f	3	Mr. Matti Rintamaki	t	35	0	0	7.125
589	t	1	Mrs. Walter Bertram (Martha Eustis) Stephenson	f	52	1	0	78.2667000000000002
590	f	3	Mr. William James Elsbury	t	47	0	0	7.25
591	f	3	Miss. Mary Bourke	f	40	0	2	7.75
592	f	2	Mr. John Henry Chapman	t	37	1	0	26
593	f	3	Mr. Jean Baptiste Van Impe	t	36	1	1	24.1499999999999986
594	t	2	Miss. Jessie Wills Leitch	f	31	0	0	33
595	f	3	Mr. Alfred Johnson	t	49	0	0	0
596	f	3	Mr. Hanna Boulos	t	18	0	0	7.22499999999999964
597	t	1	Sir. Cosmo Edmund Duff Gordon	t	49	1	0	56.9292000000000016
598	t	2	Mrs. Sidney Samuel (Amy Frances Christy) Jacobsohn	f	24	2	1	27
599	f	3	Mr. Petco Slabenoff	t	42	0	0	7.89580000000000037
600	f	1	Mr. Charles H Harrington	t	37	0	0	42.3999999999999986
601	f	3	Mr. Ernst William Torber	t	44	0	0	8.05000000000000071
602	t	1	Mr. Harry Homer	t	35	0	0	26.5500000000000007
603	f	3	Mr. Edvard Bengtsson Lindell	t	36	1	0	15.5500000000000007
604	f	3	Mr. Milan Karaic	t	30	0	0	7.89580000000000037
605	t	1	Mr. Robert Williams Daniel	t	27	0	0	30.5
606	t	2	Mrs. Joseph (Juliette Marie Louise Lafargue) Laroche	f	22	1	2	41.5792000000000002
607	t	1	Miss. Elizabeth W Shutes	f	40	0	0	153.462500000000006
608	f	3	Mrs. Anders Johan (Alfrida Konstantia Brogren) Andersson	f	39	1	5	31.2749999999999986
609	f	3	Mr. Jose Neto Jardin	t	21	0	0	7.04999999999999982
610	t	3	Miss. Margaret Jane Murphy	f	18	1	0	15.5
611	f	3	Mr. John Horgan	t	22	0	0	7.75
612	f	3	Mr. William Alfred Brocklebank	t	35	0	0	8.05000000000000071
613	t	2	Miss. Alice Herman	f	24	1	2	65
614	f	3	Mr. Ernst Gilbert Danbom	t	34	1	1	14.4000000000000004
615	f	3	Mrs. William Arthur (Cordelia K Stanlick) Lobb	f	26	1	0	16.1000000000000014
616	t	2	Miss. Marion Louise Becker	f	4	2	1	39
617	f	2	Mr. Lawrence Gavey	t	26	0	0	10.5
618	f	3	Mr. Antoni Yasbeck	t	27	1	0	14.4542000000000002
619	t	1	Mr. Edwin Nelson Jr Kimball	t	42	1	0	52.5542000000000016
620	t	3	Mr. Sahid Nakid	t	20	1	1	15.7416999999999998
621	f	3	Mr. Henry Damsgaard Hansen	t	21	0	0	7.85419999999999963
622	f	3	Mr. David John Bowen	t	21	0	0	16.1000000000000014
623	f	1	Mr. Frederick Sutton	t	61	0	0	32.3207999999999984
624	f	2	Rev. Charles Leonard Kirkland	t	57	0	0	12.3499999999999996
625	t	1	Miss. Gretchen Fiske Longley	f	21	0	0	77.9582999999999942
626	f	3	Mr. Guentcho Bostandyeff	t	26	0	0	7.89580000000000037
627	f	3	Mr. Patrick D O'Connell	t	18	0	0	7.73329999999999984
628	t	1	Mr. Algernon Henry Wilson Barkworth	t	80	0	0	30
629	f	3	Mr. Johan Svensson Lundahl	t	51	0	0	7.0541999999999998
630	t	1	Dr. Max Stahelin-Maeglin	t	32	0	0	30.5
631	f	1	Mr. William Henry Marsh Parr	t	30	0	0	0
632	f	3	Miss. Mabel Skoog	f	9	3	2	27.8999999999999986
633	t	2	Miss. Mary Davis	f	28	0	0	13
634	f	3	Mr. Antti Gustaf Leinonen	t	32	0	0	7.92499999999999982
635	f	2	Mr. Harvey Collyer	t	31	1	1	26.25
636	f	3	Mrs. Juha (Maria Emilia Ojala) Panula	f	41	0	5	39.6875
637	f	3	Mr. Percival Thorneycroft	t	37	1	0	16.1000000000000014
638	f	3	Mr. Hans Peder Jensen	t	20	0	0	7.85419999999999963
639	t	1	Mlle. Emma Sagesser	f	24	0	0	69.2999999999999972
640	f	3	Miss. Margit Elizabeth Skoog	f	2	3	2	27.8999999999999986
641	t	3	Mr. Choong Foo	t	32	0	0	56.4958000000000027
642	t	3	Miss. Eugenie Baclini	f	0.75	2	1	19.2582999999999984
643	t	1	Mr. Henry Sleeper Harper	t	48	1	0	76.7292000000000058
644	f	3	Mr. Liudevit Cor	t	19	0	0	7.89580000000000037
645	t	1	Col. Oberst Alfons Simonius-Blumer	t	56	0	0	35.5
646	f	3	Mr. Edward Willey	t	21	0	0	7.54999999999999982
647	t	3	Miss. Amy Zillah Elsie Stanley	f	23	0	0	7.54999999999999982
648	f	3	Mr. Mito Mitkoff	t	23	0	0	7.89580000000000037
649	t	2	Miss. Elsie Doling	f	18	0	1	23
650	f	3	Mr. Johannes Halvorsen Kalvik	t	21	0	0	8.43329999999999913
651	t	3	Miss. Hanora O'Leary	f	16	0	0	7.82920000000000016
652	f	3	Miss. Hanora Hegarty	f	18	0	0	6.75
653	f	2	Mr. Leonard Mark Hickman	t	24	2	0	73.5
654	f	3	Mr. Alexander Radeff	t	27	0	0	7.89580000000000037
655	f	3	Mrs. John (Catherine) Bourke	f	32	1	1	15.5
656	f	2	Mr. George Floyd Eitemiller	t	23	0	0	13
657	f	1	Mr. Arthur Webster Newell	t	58	0	2	113.275000000000006
658	t	1	Dr. Henry William Frauenthal	t	50	2	0	133.650000000000006
659	f	3	Mr. Mohamed Badt	t	40	0	0	7.22499999999999964
660	f	1	Mr. Edward Pomeroy Colley	t	47	0	0	25.5874999999999986
661	f	3	Mr. Peju Coleff	t	36	0	0	7.49580000000000002
662	t	3	Mr. Eino William Lindqvist	t	20	1	0	7.92499999999999982
663	f	2	Mr. Lewis Hickman	t	32	2	0	73.5
664	f	2	Mr. Reginald Fenton Butler	t	25	0	0	13
665	f	3	Mr. Knud Paust Rommetvedt	t	49	0	0	7.77500000000000036
666	f	3	Mr. Jacob Cook	t	43	0	0	8.05000000000000071
667	t	1	Mrs. Elmer Zebley (Juliet Cummins Wright) Taylor	f	48	1	0	52
668	t	2	Mrs. Thomas William Solomon (Elizabeth Catherine Ford) Brown	f	40	1	1	39
669	f	1	Mr. Thornton Davidson	t	31	1	0	52
670	f	2	Mr. Henry Michael Mitchell	t	70	0	0	10.5
671	t	2	Mr. Charles Wilhelms	t	31	0	0	13
672	f	2	Mr. Ennis Hastings Watson	t	19	0	0	0
673	f	3	Mr. Gustaf Hjalmar Edvardsson	t	18	0	0	7.77500000000000036
674	f	3	Mr. Frederick Charles Sawyer	t	24.5	0	0	8.05000000000000071
675	t	3	Miss. Anna Sofia Turja	f	18	0	0	9.84169999999999945
676	f	3	Mrs. Frederick (Augusta Tyler) Goodwin	f	43	1	6	46.8999999999999986
677	t	1	Mr. Thomas Drake Martinez Cardeza	t	36	0	1	512.329200000000014
678	f	3	Miss. Katie Peters	f	28	0	0	8.13749999999999929
679	t	1	Mr. Hammad Hassab	t	27	0	0	76.7292000000000058
680	f	3	Mr. Thor Anderson Olsvigen	t	20	0	0	9.22499999999999964
681	f	3	Mr. Charles Edward Goodwin	t	14	5	2	46.8999999999999986
682	f	2	Mr. Thomas William Solomon Brown	t	60	1	1	39
683	f	2	Mr. Joseph Philippe Lemercier Laroche	t	25	1	2	41.5792000000000002
684	f	3	Mr. Jaako Arnold Panula	t	14	4	1	39.6875
685	f	3	Mr. Branko Dakic	t	19	0	0	10.1707999999999998
686	f	3	Mr. Eberhard Thelander Fischer	t	18	0	0	7.79579999999999984
687	t	1	Miss. Georgette Alexandra Madill	f	15	0	1	211.337500000000006
688	t	1	Mr. Albert Adrian Dick	t	31	1	0	57
689	t	3	Miss. Manca Karun	f	4	0	1	13.4167000000000005
690	t	3	Mr. Ali Lam	t	37	0	0	56.4958000000000027
691	f	3	Mr. Khalil Saad	t	25	0	0	7.22499999999999964
692	f	1	Col. John Weir	t	60	0	0	26.5500000000000007
693	f	2	Mr. Charles Henry Chapman	t	52	0	0	13.5
694	f	3	Mr. James Kelly	t	44	0	0	8.05000000000000071
695	t	3	Miss. Katherine Mullens	f	19	0	0	7.73329999999999984
696	f	1	Mr. John Borland Thayer	t	49	1	1	110.883300000000006
697	f	3	Mr. Adolf Mathias Nicolai Olsen Humblen	t	42	0	0	7.65000000000000036
698	t	1	Mrs. John Jacob (Madeleine Talmadge Force) Astor	f	18	1	0	227.525000000000006
699	t	1	Mr. Spencer Victor Silverthorne	t	35	0	0	26.2875000000000014
700	f	3	Miss. Saiide Barbara	f	18	0	1	14.4542000000000002
701	f	3	Mr. Martin Gallagher	t	25	0	0	7.7416999999999998
702	f	3	Mr. Henrik Juul Hansen	t	26	1	0	7.85419999999999963
703	f	2	Mr. Henry Samuel Morley	t	39	0	0	26
704	t	2	Mrs. Florence Kelly	f	45	0	0	13.5
705	t	1	Mr. Edward Pennington Calderhead	t	42	0	0	26.2875000000000014
706	t	1	Miss. Alice Cleaver	f	22	0	0	151.550000000000011
707	t	3	Master. Halim Gonios Moubarek	t	4	1	1	15.2457999999999991
708	t	1	Mlle. Berthe Antonine Mayne	f	24	0	0	49.5041999999999973
709	f	1	Mr. Herman Klaber	t	41	0	0	26.5500000000000007
710	t	1	Mr. Elmer Zebley Taylor	t	48	1	0	52
711	f	3	Mr. August Viktor Larsson	t	29	0	0	9.48329999999999984
712	f	2	Mr. Samuel Greenberg	t	52	0	0	13
713	f	3	Mr. Peter Andreas Lauritz Andersen Soholt	t	19	0	0	7.65000000000000036
714	t	1	Miss. Caroline Louise Endres	f	38	0	0	227.525000000000006
715	t	2	Miss. Edwina Celia Troutt	f	27	0	0	10.5
716	f	3	Mr. Malkolm Joackim Johnson	t	33	0	0	7.77500000000000036
717	t	2	Miss. Annie Jessie Harper	f	6	0	1	33
718	f	3	Mr. Svend Lauritz Jensen	t	17	1	0	7.0541999999999998
719	f	2	Mr. William Henry Gillespie	t	34	0	0	13
720	f	2	Mr. Henry Price Hodges	t	50	0	0	13
721	t	1	Mr. Norman Campbell Chambers	t	27	1	0	53.1000000000000014
722	f	3	Mr. Luka Oreskovic	t	20	0	0	8.66249999999999964
723	t	2	Mrs. Peter Henry (Lillian Jefferys) Renouf	f	30	3	0	21
724	t	3	Miss. Margareth Mannion	f	28	0	0	7.73749999999999982
725	f	2	Mr. Kurt Arnold Gottfrid Bryhl	t	25	1	0	26
726	f	3	Miss. Pieta Sofia Ilmakangas	f	25	1	0	7.92499999999999982
727	t	1	Miss. Elisabeth Walton Allen	f	29	0	0	211.337500000000006
728	f	3	Mr. Houssein G N Hassan	t	11	0	0	18.7875000000000014
729	f	2	Mr. Robert J Knight	t	41	0	0	0
730	f	2	Mr. William John Berriman	t	23	0	0	13
731	f	2	Mr. Moses Aaron Troupiansky	t	23	0	0	13
732	f	3	Mr. Leslie Williams	t	28.5	0	0	16.1000000000000014
733	f	3	Mrs. Edward (Margaret Ann Watson) Ford	f	48	1	3	34.375
734	t	1	Mr. Gustave J Lesurer	t	35	0	0	512.329200000000014
735	f	3	Mr. Kanio Ivanoff	t	20	0	0	7.89580000000000037
736	f	3	Mr. Minko Nankoff	t	32	0	0	7.89580000000000037
737	t	1	Mr. Walter James Hawksford	t	45	0	0	30
738	f	1	Mr. Tyrell William Cavendish	t	36	1	0	78.8499999999999943
739	t	1	Miss. Susan Parker Ryerson	f	21	2	2	262.375
740	f	3	Mr. Neal McNamee	t	24	1	0	16.1000000000000014
741	t	3	Mr. Juho Stranden	t	31	0	0	7.92499999999999982
742	f	1	Capt. Edward Gifford Crosby	t	70	1	1	71
743	f	3	Mr. Rossmore Edward Abbott	t	16	1	1	20.25
744	t	2	Miss. Anna Sinkkonen	f	30	0	0	13
745	f	1	Mr. Daniel Warner Marvin	t	19	1	0	53.1000000000000014
746	f	3	Mr. Michael Connaghton	t	31	0	0	7.75
747	t	2	Miss. Joan Wells	f	4	1	1	23
748	t	3	Master. Meier Moor	t	6	0	1	12.4749999999999996
749	f	3	Mr. Johannes Joseph Vande Velde	t	33	0	0	9.5
750	f	3	Mr. Lalio Jonkoff	t	23	0	0	7.89580000000000037
751	t	2	Mrs. Samuel (Jane Laver) Herman	f	48	1	2	65
752	t	2	Master. Viljo Hamalainen	t	0.67000000000000004	1	1	14.5
753	f	3	Mr. August Sigfrid Carlsson	t	28	0	0	7.79579999999999984
754	f	2	Mr. Percy Andrew Bailey	t	18	0	0	11.5
755	f	3	Mr. Thomas Leonard Theobald	t	34	0	0	8.05000000000000071
756	t	1	the Countess. of (Lucy Noel Martha Dyer-Edwards) Rothes	f	33	0	0	86.5
757	f	3	Mr. John Garfirth	t	23	0	0	14.5
758	f	3	Mr. Iisakki Antino Aijo Nirva	t	41	0	0	7.125
759	t	3	Mr. Hanna Assi Barah	t	20	0	0	7.22919999999999963
760	t	1	Mrs. William Ernest (Lucile Polk) Carter	f	36	1	2	120
761	f	3	Mr. Hans Linus Eklund	t	16	0	0	7.77500000000000036
762	t	1	Mrs. John C (Anna Andrews) Hogeboom	f	51	1	0	77.9582999999999942
763	f	1	Dr. Arthur Jackson Brewe	t	46	0	0	39.6000000000000014
764	f	3	Miss. Mary Mangan	f	30.5	0	0	7.75
765	f	3	Mr. Daniel J Moran	t	28	1	0	24.1499999999999986
766	f	3	Mr. Daniel Danielsen Gronnestad	t	32	0	0	8.36250000000000071
767	f	3	Mr. Rene Aime Lievens	t	24	0	0	9.5
768	f	3	Mr. Niels Peder Jensen	t	48	0	0	7.85419999999999963
769	f	2	Mrs. (Mary) Mack	f	57	0	0	10.5
770	f	3	Mr. Dibo Elias	t	29	0	0	7.22499999999999964
771	t	2	Mrs. Elizabeth (Eliza Needs) Hocking	f	54	1	3	23
772	f	3	Mr. Pehr Fabian Oliver Malkolm Myhrman	t	18	0	0	7.75
773	f	3	Mr. Roger Tobin	t	20	0	0	7.75
774	t	3	Miss. Virginia Ethel Emanuel	f	5	0	0	12.4749999999999996
775	f	3	Mr. Thomas J Kilgannon	t	22	0	0	7.73749999999999982
776	t	1	Mrs. Edward Scott (Elisabeth Walton McMillan) Robert	f	43	0	1	211.337500000000006
777	t	3	Miss. Banoura Ayoub	f	13	0	0	7.22919999999999963
778	t	1	Mrs. Albert Adrian (Vera Gillespie) Dick	f	17	1	0	57
779	f	1	Mr. Milton Clyde Long	t	29	0	0	30
780	f	3	Mr. Andrew G Johnston	t	35	1	2	23.4499999999999993
781	f	3	Mr. William Ali	t	25	0	0	7.04999999999999982
782	f	3	Mr. Abraham (David Lishin) Harmer	t	25	0	0	7.25
783	t	3	Miss. Anna Sofia Sjoblom	f	18	0	0	7.49580000000000002
784	f	3	Master. George Hugh Rice	t	8	4	1	29.125
785	t	3	Master. Bertram Vere Dean	t	1	1	2	20.5749999999999993
786	f	1	Mr. Benjamin Guggenheim	t	46	0	0	79.2000000000000028
787	f	3	Mr. Andrew Keane	t	20	0	0	7.75
788	f	2	Mr. Alfred Gaskell	t	16	0	0	26
789	f	3	Miss. Stella Anna Sage	f	21	8	2	69.5499999999999972
790	f	1	Mr. William Fisher Hoyt	t	43	0	0	30.6957999999999984
791	f	3	Mr. Ristiu Dantcheff	t	25	0	0	7.89580000000000037
792	f	2	Mr. Richard Otter	t	39	0	0	13
793	t	1	Dr. Alice (Farnham) Leader	f	49	0	0	25.9292000000000016
794	t	3	Mrs. Mara Osman	f	31	0	0	8.68329999999999913
795	f	3	Mr. Yousseff Ibrahim Shawah	t	30	0	0	7.22919999999999963
796	f	3	Mrs. Jean Baptiste (Rosalie Paula Govaert) Van Impe	f	30	1	1	24.1499999999999986
797	f	2	Mr. Martin Ponesell	t	34	0	0	13
798	t	2	Mrs. Harvey (Charlotte Annie Tate) Collyer	f	31	1	1	26.25
799	t	1	Master. William Thornton II Carter	t	11	1	2	120
800	t	3	Master. Assad Alexander Thomas	t	0.419999999999999984	0	1	8.51670000000000016
801	t	3	Mr. Oskar Arvid Hedman	t	27	0	0	6.97499999999999964
802	f	3	Mr. Karl Johan Johansson	t	31	0	0	7.77500000000000036
803	f	1	Mr. Thomas Jr Andrews	t	39	0	0	0
804	f	3	Miss. Ellen Natalia Pettersson	f	18	0	0	7.77500000000000036
805	f	2	Mr. August Meyer	t	39	0	0	13
806	t	1	Mrs. Norman Campbell (Bertha Griggs) Chambers	f	33	1	0	53.1000000000000014
807	f	3	Mr. William Alexander	t	26	0	0	7.88750000000000018
808	f	3	Mr. James Lester	t	39	0	0	24.1499999999999986
809	f	2	Mr. Richard James Slemen	t	35	0	0	10.5
810	f	3	Miss. Ebba Iris Alfrida Andersson	f	6	4	2	31.2749999999999986
811	f	3	Mr. Ernest Portage Tomlin	t	30.5	0	0	8.05000000000000071
812	f	1	Mr. Richard Fry	t	39	0	0	0
813	f	3	Miss. Wendla Maria Heininen	f	23	0	0	7.92499999999999982
814	f	2	Mr. Albert Mallet	t	31	1	1	37.0041999999999973
815	f	3	Mr. John Fredrik Alexander Holm	t	43	0	0	6.45000000000000018
816	f	3	Master. Karl Thorsten Skoog	t	10	3	2	27.8999999999999986
817	t	1	Mrs. Charles Melville (Clara Jennings Gregg) Hays	f	52	1	1	93.5
818	t	3	Mr. Nikola Lulic	t	27	0	0	8.66249999999999964
819	f	1	Jonkheer. John George Reuchlin	t	38	0	0	0
820	t	3	Mrs. (Beila) Moor	f	27	0	1	12.4749999999999996
821	f	3	Master. Urho Abraham Panula	t	2	4	1	39.6875
822	f	3	Mr. John Flynn	t	36	0	0	6.95000000000000018
823	f	3	Mr. Len Lam	t	23	0	0	56.4958000000000027
824	t	2	Master. Andre Mallet	t	1	0	2	37.0041999999999973
825	t	3	Mr. Thomas Joseph McCormack	t	19	0	0	7.75
826	t	1	Mrs. George Nelson (Martha Evelyn) Stone	f	62	0	0	80
827	t	3	Mrs. Antoni (Selini Alexander) Yasbeck	f	15	1	0	14.4542000000000002
828	t	2	Master. George Sibley Richards	t	0.82999999999999996	1	1	18.75
829	f	3	Mr. Amin Saad	t	30	0	0	7.22919999999999963
830	f	3	Mr. Albert Augustsson	t	23	0	0	7.85419999999999963
831	f	3	Mr. Owen George Allum	t	18	0	0	8.30000000000000071
832	t	1	Miss. Sara Rebecca Compton	f	39	1	1	83.158299999999997
833	f	3	Mr. Jakob Pasic	t	21	0	0	8.66249999999999964
834	f	3	Mr. Maurice Sirota	t	20	0	0	8.05000000000000071
835	t	3	Mr. Chang Chip	t	32	0	0	56.4958000000000027
836	t	1	Mr. Pierre Marechal	t	29	0	0	29.6999999999999993
837	f	3	Mr. Ilmari Rudolf Alhomaki	t	20	0	0	7.92499999999999982
838	f	2	Mr. Thomas Charles Mudd	t	16	0	0	10.5
839	t	1	Miss. Augusta Serepeca	f	30	0	0	31
840	f	3	Mr. Peter L Lemberopolous	t	34.5	0	0	6.4375
841	f	3	Mr. Jeso Culumovic	t	17	0	0	8.66249999999999964
842	f	3	Mr. Anthony Abbing	t	42	0	0	7.54999999999999982
843	f	3	Mr. Douglas Bullen Sage	t	18	8	2	69.5499999999999972
844	f	3	Mr. Marin Markoff	t	35	0	0	7.89580000000000037
845	f	2	Rev. John Harper	t	28	0	1	33
846	t	1	Mrs. Samuel L (Edwiga Grabowska) Goldenberg	f	40	1	0	89.1042000000000058
847	f	3	Master. Sigvard Harald Elias Andersson	t	4	4	2	31.2749999999999986
848	f	3	Mr. Johan Svensson	t	74	0	0	7.77500000000000036
849	f	3	Miss. Nourelain Boulos	f	9	1	1	15.2457999999999991
850	t	1	Miss. Mary Conover Lines	f	16	0	1	39.3999999999999986
851	f	2	Mrs. Ernest Courtenay (Lilian Hughes) Carter	f	44	1	0	26
852	t	3	Mrs. Sam (Leah Rosen) Aks	f	18	0	1	9.34999999999999964
853	t	1	Mrs. George Dennick (Mary Hitchcock) Wick	f	45	1	1	164.866700000000009
854	t	1	Mr. Peter Denis Daly	t	51	0	0	26.5500000000000007
855	t	3	Mrs. Solomon (Latifa Qurban) Baclini	f	24	0	3	19.2582999999999984
856	f	3	Mr. Raihed Razi	t	30	0	0	7.22919999999999963
857	f	3	Mr. Claus Peter Hansen	t	41	2	0	14.1082999999999998
858	f	2	Mr. Frederick Edward Giles	t	21	1	0	11.5
859	t	1	Mrs. Frederick Joel (Margaret Welles Barron) Swift	f	48	0	0	25.9292000000000016
860	f	3	Miss. Dorothy Edith Sage	f	14	8	2	69.5499999999999972
861	f	2	Mr. John William Gill	t	24	0	0	13
862	t	2	Mrs. (Karolina) Bystrom	f	42	0	0	13
863	t	2	Miss. Asuncion Duran y More	f	27	1	0	13.8582999999999998
864	f	1	Mr. Washington Augustus II Roebling	t	31	0	0	50.4958000000000027
865	f	3	Mr. Philemon van Melkebeke	t	23	0	0	9.5
866	t	3	Master. Harold Theodor Johnson	t	4	1	1	11.1333000000000002
867	f	3	Mr. Cerin Balkic	t	26	0	0	7.89580000000000037
868	t	1	Mrs. Richard Leonard (Sallie Monypeny) Beckwith	f	47	1	1	52.5542000000000016
869	f	1	Mr. Frans Olof Carlsson	t	33	0	0	5
870	f	3	Mr. Victor Vander Cruyssen	t	47	0	0	9
871	t	2	Mrs. Samuel (Hannah Wizosky) Abelson	f	28	1	0	24
872	t	3	Miss. Adele Kiamie Najib	f	15	0	0	7.22499999999999964
873	f	3	Mr. Alfred Ossian Gustafsson	t	20	0	0	9.84580000000000055
874	f	3	Mr. Nedelio Petroff	t	19	0	0	7.89580000000000037
875	f	3	Mr. Kristo Laleff	t	23	0	0	7.89580000000000037
876	t	1	Mrs. Thomas Jr (Lily Alexenia Wilson) Potter	f	56	0	1	83.158299999999997
877	t	2	Mrs. William (Imanita Parrish Hall) Shelley	f	25	0	1	26
878	f	3	Mr. Johann Markun	t	33	0	0	7.89580000000000037
879	f	3	Miss. Gerda Ulrika Dahlberg	f	22	0	0	10.5167000000000002
880	f	2	Mr. Frederick James Banfield	t	28	0	0	10.5
881	f	3	Mr. Henry Jr Sutehall	t	25	0	0	7.04999999999999982
882	f	3	Mrs. William (Margaret Norton) Rice	f	39	0	5	29.125
883	f	2	Rev. Juozas Montvila	t	27	0	0	13
884	t	1	Miss. Margaret Edith Graham	f	19	0	0	30
885	f	3	Miss. Catherine Helen Johnston	f	7	1	2	23.4499999999999993
886	t	1	Mr. Karl Howell Behr	t	26	0	0	30
887	f	3	Mr. Patrick Dooley	t	32	0	0	7.75
\.


--
-- TOC entry 2818 (class 0 OID 0)
-- Dependencies: 196
-- Name: titanic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.titanic_id_seq', 887, true);


--
-- TOC entry 2688 (class 2606 OID 16587)
-- Name: titanic titanic_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.titanic
    ADD CONSTRAINT titanic_pkey PRIMARY KEY (id);


-- Completed on 2019-02-19 18:56:26

--
-- PostgreSQL database dump complete
--

