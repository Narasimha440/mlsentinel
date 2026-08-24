"""
MLSentinel SDK error codes.

This module contains the error, warning, and limit codes used by
the MLSentinel SDK and platform.

Each code is represented by a unique string identifier beginning
with ``MLS``. These codes can be used to identify and categorize
errors and warnings consistently across the SDK and API.

Error code categories
---------------------

Authentication errors:
    MLS001 - MLS009

Network errors:
    MLS010 - MLS019

Validation errors:
    MLS020 - MLS037

Server errors:
    MLS040 - MLS059

SDK errors:
    MLS060 - MLS079

Warnings and limits:
    MLS080 - MLS099

Example
-------
>>> from mlsentinel.error_codes import ErrorCodes

>>> ErrorCodes.INVALID_API_KEY
'MLS001'
"""


class ErrorCodes:
    """
    Collection of MLSentinel SDK error and warning codes.

    The constants in this class are grouped by category to make
    it easier to identify the source and type of an SDK or API
    problem.

    Notes
    -----
    These constants are identifiers only. The actual handling of
    an error or warning is performed by the relevant SDK or API
    component.
    """

    # ------------------------------------------------------------------
    # AUTHENTICATION ERROR CODES
    # ------------------------------------------------------------------

    INVALID_API_KEY = "MLS001"
    API_KEY_MISSING = "MLS002"
    API_KEY_EXPIRED = "MLS003"
    API_KEY_REVOKED = "MLS004"
    ACCESS_DENIED = "MLS005"
    API_KEY_INVALID = "MLS006"
    INSUFFICIENT_PERMISSIONS = "MLS007"
    ACCOUNT_SUSPENDED = "MLS008"
    AUTHENTICATION_FAILED = "MLS009"

    # ------------------------------------------------------------------
    # NETWORK ERROR CODES
    # ------------------------------------------------------------------

    MLSENTINAL_CONNECTION_ERROR = "MLS010"
    REQUEST_TIME_OUT = "MLS011"
    HANDSHAKE_FAILED = "MLS012"
    DNS_LOOKUP_FAILED = "MLS013"
    NETWORK_CONNECTION_FAILED = "MLS014"
    SERVER_CONNECTION_CLOSED = "MLS015"
    PROXY_CONNECTION_FAILED = "MLS016"
    INVALID_BACKEND_URL = "MLS017"
    RETRIES_EXCEEDED = "MLS018"
    UNKNOWN_NETWORK_ERROR = "MLS019"

    # ------------------------------------------------------------------
    # VALIDATION ERROR CODES
    # ------------------------------------------------------------------

    PROJECT_NAME_REQUIRED = "MLS020"
    PROJECT_NAME_INVALID = "MLS021"
    MODEL_NAME_REQUIRED = "MLS022"
    MODEL_NAME_INVALID = "MLS023"
    METRICS_REQUIRED = "MLS024"
    METRICS_MUST_DICT = "MLS025"
    REQUIRED_METRIC_MISSING = "MLS026"
    METRIC_VALUE_BE_NUMERIC = "MLS025"
    METRIC_OUT_RANGE = "MLS026"
    METRIC_UNSUPPORTED = "MLS027"
    PAYLOAD_EMPTY = "MLS028"
    PAYLOAD_FORMAT_INVALID = "MLS029"
    JSON_SERIALIZATION_FAILED = "MLS030"
    DUPLICATE_METRIC = "MLS031"
    INVALID_PROJECT_CONFIGURATION = "MLS032"
    INVALID_SDK_CONFIGURATION = "MLS033"
    DATASET_INFORMATION_INVALID = "MLS034"
    MODEL_VERSION_INVALID = "MLS035"
    INVALID_REQUEST_PARAMETER = "MLS036"
    VALIDATION_FAILED = "MLS037"

    # ------------------------------------------------------------------
    # INTERNAL SERVER ERROR CODES
    # ------------------------------------------------------------------

    INTERNAL_SERVER_ERROR = "MLS040"
    SERVER_TEMPORARY_UNAVAILABLE = "MLS041"
    ANALYSIS_ENGINE_FAILED = "MLS042"
    SERVER_INVALID_RESPONSE = "MLS043"
    DATABASE_OPERATION_FAILED = "MLS044"
    REPORT_GENERATION_FAILED = "MLS045"
    AI_ANALYSIS_FAILED = "MLS046"
    MODEL_EVALUATION_FAILED = "MLS047"
    SERVER_CONFIGURATION_FAILED = "MLS048"
    REQUEST_PROCESS_FAILED = "MLS049"
    RATE_LIMIT_EXCEEDED = "MLS050"
    ENDPOINT_NOT_EXIST = "MLS051"
    RESOURCE_NOT_FOUND = "MLS052"
    UNSUPPORT_API_VERSION = "MLS053"
    BACKEND_MAINTENANCE = "MLS054"
    STORAGE_SERVICE_UNAVAILABLE = "MLS055"
    QUEUE_PROCESS_FAILED = "MLS056"
    REPORT_UNAVAILABLE = "MLS057"
    ANALYSIS_REQUEST_CANCELLED = "MLS058"
    UNKNOWN_SERVER_ERROR = "MLS059"

    # ------------------------------------------------------------------
    # SDK ERRORS
    # ------------------------------------------------------------------

    INITIALIZATION_FAILED = "MLS060"
    SDK_CONFIGURATION_MISSED = "MLS061"
    UNSUPPORTED_SDK_VERSION = "MLS062"
    SDK_UNEXCEPTED_ERROR = "MLS063"
    FAILED_SDK_CONFIGURATION = "MLS064"
    SDK_CACHE_ERROR = "MLS065"
    SDK_SERIALIZATION_FAILED = "MLS066"
    SDK_DESERIALIZATION_FAILED = "MLS067"
    UNSUPPORTED_PYTHON_VERSION = "MLS068"
    DEPENDENCY_MISSING = "MLS069"
    DEPENDENCY_VERSION_MISMATCH = "MLS070"
    LOGGER_INITIALIZATION_FAILED = "MLS071"
    PLUGIN_LOADING_FAILED = "MLS072"
    ENV_CONF_MISSING = "MLS073"
    UNSUPPORT_FEATUED = "MLS074"
    SDK_INTEGRITY_CHECK_FAILED = "MLS075"
    LICENSE_VALIDATION_FAILED = "MLS076"
    LOCAL_CACHE_CORRUPTED = "MLS077"
    RETRY_LIMIT_REACHED = "MLS078"
    UNKNOWN_SDK_ERROR = "MLS079"

    # ------------------------------------------------------------------
    # MLSENTINEL WARNINGS AND LIMITS
    # ------------------------------------------------------------------

    PREFORMANCE_BELOW_THRESHOLD = "MLS080"
    OPTIONAL_METRICS_MISS = "MLS081"
    LARGE_PAYLOAD_DETECTED = "MLS082"
    DEPRECATED_SDK_METHOD = "MLS083"
    DEPRECATED_API_ENDPOINT = "MLS084"
    BACKEND_RESPONSE_DELAYED = "MLS085"
    PARTIAL_ANALYSIS_COMPLETED = "MLS086"
    SOME_REC_UNAVAILABLE = "MLS087"
    LIMITED_ANALYSIS_PERFORMED = "MLS088"
    EXPERIMENTAL_FEATURE_ENABLED = "MLS089"
    APPROACHING_RATE_LIMIT = "MLS090"
    SDK_UPDATE_AVAILABLE = "MLS091"
    ANALYSIS_BASED_INCOMPLETE_METRICS = "MLS092"
    LOCAL_FALLBACK_MODE_ENABLED = "MLS093"
    BACKEND_COMPATIBILITY_WARNING = "MLS094"
    UNKNOWN_WARNING = "MLS095"
    RESPONSE_WITH_DEPRECATED_FEILDS = "MLS096"
    OPTIONAL_DEPENDENCY_MISSING = "MLS097"
    FEATURE_DISABLED_WITH_SERVER_POLICY = "MLS098"
    GENERAL_SDK_WARNING = "MLS099"