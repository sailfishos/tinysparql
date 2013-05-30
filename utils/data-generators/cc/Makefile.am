include $(top_srcdir)/Makefile.decl

EXTRA_DIST =                                           \
	default.cfg                                    \
	gen_data.py                                    \
	generate                                       \
	__init__.py                                    \
	max.cfg                                        \
	mfo.py                                         \
	mlo.py                                         \
	mto.py                                         \
	ncal.py                                        \
	nco.py                                         \
	nfo.py                                         \
	nmm.py                                         \
	nmo.py                                         \
	slo.py                                         \
	ontology_prefixes.py                           \
	tools.py                                       \
	tracker.py                                     \
	convert_data.py                                \
	source-data

nemotestsdir = /opt/tests/tracker/bin
nemotests_DATA = default.cfg max.cfg
nemotests_SCRIPTS = generate
nemotests_PYTHON = gen_data.py __init__.py mfo.py mlo.py mto.py ncal.py nco.py nfo.py nmm.py \
                   nmo.py slo.py ontology_prefixes.py tools.py tracker.py convert_data.py

nemotestdatadir = /opt/tests/tracker/bin/source-data
nemotestdata_DATA = source-data/area-codes.txt source-data/equipment-manufacturers.txt source-data/job-titles.txt source-data/male-prefix.txt \
                    source-data/company-names.txt source-data/equipment-models.txt source-data/last-name.txt source-data/street-names.txt \
                    source-data/company-types.txt source-data/female-first-name.txt source-data/latin-words.txt source-data/street-types.txt \
                    source-data/email-domains.txt source-data/female-prefix.txt source-data/male-first-name.txt source-data/zip-codes.txt
