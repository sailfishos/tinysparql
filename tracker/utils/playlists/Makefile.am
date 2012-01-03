include $(top_srcdir)/Makefile.decl

noinst_PROGRAMS = playlist2ttl

AM_CPPFLAGS =                                          \
	$(BUILD_CFLAGS)                                \
	$(TOTEM_PL_PARSER_CFLAGS)

LDADD =                                                \
	$(BUILD_LIBS)                                  \
	$(TOTEM_PL_PARSER_LIBS)                        \
	-lgio-2.0

playlist2ttl_SOURCES =                                 \
	playlist2ttl.c

