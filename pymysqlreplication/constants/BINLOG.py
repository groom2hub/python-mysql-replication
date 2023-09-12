# -*- coding: utf-8 -*-

UNKNOWN_EVENT = 0x00
START_EVENT_V3 = 0x01
QUERY_EVENT = 0x02
STOP_EVENT = 0x03
ROTATE_EVENT = 0x04
INTVAR_EVENT = 0x05
LOAD_EVENT = 0x06
SLAVE_EVENT = 0x07
CREATE_FILE_EVENT = 0x08
APPEND_BLOCK_EVENT = 0x09
EXEC_LOAD_EVENT = 0x0A
DELETE_FILE_EVENT = 0x0B
NEW_LOAD_EVENT = 0x0C
RAND_EVENT = 0x0D
USER_VAR_EVENT = 0x0E
FORMAT_DESCRIPTION_EVENT = 0x0F
XID_EVENT = 0x10
BEGIN_LOAD_QUERY_EVENT = 0x11
EXECUTE_LOAD_QUERY_EVENT = 0x12
TABLE_MAP_EVENT = 0x13
PRE_GA_WRITE_ROWS_EVENT = 0x14
PRE_GA_UPDATE_ROWS_EVENT = 0x15
PRE_GA_DELETE_ROWS_EVENT = 0x16
WRITE_ROWS_EVENT_V1 = 0x17
UPDATE_ROWS_EVENT_V1 = 0x18
DELETE_ROWS_EVENT_V1 = 0x19
INCIDENT_EVENT = 0x1A
HEARTBEAT_LOG_EVENT = 0x1B
IGNORABLE_LOG_EVENT = 0x1C
ROWS_QUERY_LOG_EVENT = 0x1D
WRITE_ROWS_EVENT_V2 = 0x1E
UPDATE_ROWS_EVENT_V2 = 0x1F
DELETE_ROWS_EVENT_V2 = 0x20
GTID_LOG_EVENT = 0x21
ANONYMOUS_GTID_LOG_EVENT = 0x22
PREVIOUS_GTIDS_LOG_EVENT = 0x23
XA_PREPARE_EVENT = 0x26

# INTVAR types
INTVAR_INVALID_INT_EVENT = 0x00
INTVAR_LAST_INSERT_ID_EVENT = 0x01
INTVAR_INSERT_ID_EVENT = 0x02

# MariaDB events
MARIADB_ANNOTATE_ROWS_EVENT = 0xA0
MARIADB_BINLOG_CHECKPOINT_EVENT = 0xA1
MARIADB_GTID_EVENT = 0xA2
MARIADB_GTID_GTID_LIST_EVENT = 0xA3
MARIADB_START_ENCRYPTION_EVENT = 0xA4

# Common-Footer
BINLOG_CHECKSUM_LEN = 4
