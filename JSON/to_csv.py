import json
import pandas as pd

# JSON data
data = {
"results" : [ {
      "ruleId" : "py/bind-socket-all-network-interfaces",
      "ruleIndex" : 1,
      "rule" : {
        "id" : "py/bind-socket-all-network-interfaces",
        "index" : 1
      },
      "message" : {
        "text" : "'' binds a socket to all interfaces."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/contrib/opt/python/training/variable_clipping_optimizer_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 0
          },
          "region" : {
            "startLine" : 42,
            "startColumn" : 7,
            "endColumn" : 22
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "c8941f2cb283c3a7:1",
        "primaryLocationStartColumnFingerprint" : "0"
      }
    }, {
      "ruleId" : "py/insecure-protocol",
      "ruleIndex" : 21,
      "rule" : {
        "id" : "py/insecure-protocol",
        "index" : 21
      },
      "message" : {
        "text" : "Insecure SSL/TLS protocol version TLSv1 allowed by [call to ssl.SSLContext](1).\nInsecure SSL/TLS protocol version TLSv1_1 allowed by [call to ssl.SSLContext](1)."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/contrib/ignite/python/ops/ignite_dataset_ops.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 1
          },
          "region" : {
            "startLine" : 122,
            "startColumn" : 19,
            "endColumn" : 26
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "bc20f03accee468e:1",
        "primaryLocationStartColumnFingerprint" : "12"
      },
      "relatedLocations" : [ {
        "id" : 1,
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/contrib/ignite/python/ops/ignite_dataset_ops.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 1
          },
          "region" : {
            "startLine" : 120,
            "startColumn" : 17,
            "endColumn" : 52
          }
        },
        "message" : {
          "text" : "call to ssl.SSLContext"
        }
      } ]
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/contrib/rnn/python/tools/checkpoint_convert_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 2
          },
          "region" : {
            "startLine" : 35,
            "startColumn" : 27,
            "endColumn" : 44
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "9d851b3f98d66425:1",
        "primaryLocationStartColumnFingerprint" : "22"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/contrib/rnn/python/tools/checkpoint_convert_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 2
          },
          "region" : {
            "startLine" : 36,
            "startColumn" : 27,
            "endColumn" : 44
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "a30e46177065df84:1",
        "primaryLocationStartColumnFingerprint" : "22"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/cli/curses_ui_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 3
          },
          "region" : {
            "startLine" : 94,
            "startColumn" : 27,
            "endColumn" : 44
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "9fa330944120513f:1",
        "primaryLocationStartColumnFingerprint" : "18"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/cli/curses_ui_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 3
          },
          "region" : {
            "startLine" : 1223,
            "startColumn" : 19,
            "endColumn" : 36
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "302a6b1be3e17bd7:1",
        "primaryLocationStartColumnFingerprint" : "14"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/cli/curses_ui_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 3
          },
          "region" : {
            "startLine" : 1260,
            "startColumn" : 19,
            "endColumn" : 36
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "302a6b1be3e17bd7:2",
        "primaryLocationStartColumnFingerprint" : "14"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/lib/debug_data_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 4
          },
          "region" : {
            "startLine" : 154,
            "startColumn" : 23,
            "endColumn" : 40
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "ef06a45dc9d58733:1",
        "primaryLocationStartColumnFingerprint" : "18"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/lib/debug_data_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 4
          },
          "region" : {
            "startLine" : 186,
            "startColumn" : 31,
            "endColumn" : 48
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "e4c62e6a2374c97b:1",
        "primaryLocationStartColumnFingerprint" : "24"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/examples/debug_errors.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 5
          },
          "region" : {
            "startLine" : 45,
            "startColumn" : 25,
            "endColumn" : 57
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "78e5e7cebce66ba1:1",
        "primaryLocationStartColumnFingerprint" : "20"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/examples/debug_keras.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 6
          },
          "region" : {
            "startLine" : 45,
            "startColumn" : 25,
            "endColumn" : 57
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "78e5e7cebce66ba1:1",
        "primaryLocationStartColumnFingerprint" : "20"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/examples/debug_mnist.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 7
          },
          "region" : {
            "startLine" : 129,
            "startColumn" : 25,
            "endColumn" : 57
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "78e5e7cebce66ba1:1",
        "primaryLocationStartColumnFingerprint" : "20"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/examples/debug_tflearn_iris.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 8
          },
          "region" : {
            "startLine" : 61,
            "startColumn" : 25,
            "endColumn" : 57
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "78e5c58554c134d8:1",
        "primaryLocationStartColumnFingerprint" : "20"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/cli/debugger_cli_common_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 9
          },
          "region" : {
            "startLine" : 256,
            "startColumn" : 17,
            "endColumn" : 34
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "28e5aeefb06908e5:1",
        "primaryLocationStartColumnFingerprint" : "12"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/cli/debugger_cli_common_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 9
          },
          "region" : {
            "startLine" : 933,
            "startColumn" : 31,
            "endColumn" : 48
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "190ba8fd0aed851:1",
        "primaryLocationStartColumnFingerprint" : "26"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/keras/distribute/keras_utils_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 10
          },
          "region" : {
            "startLine" : 560,
            "startColumn" : 24,
            "endColumn" : 46
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "7bbf1e70425d707b:1",
        "primaryLocationStartColumnFingerprint" : "15"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/keras/distribute/keras_utils_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 10
          },
          "region" : {
            "startLine" : 596,
            "startColumn" : 24,
            "endColumn" : 41
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "4db1fbfd091933a2:1",
        "primaryLocationStartColumnFingerprint" : "15"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/saved_model/load_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 11
          },
          "region" : {
            "startLine" : 194,
            "startColumn" : 16,
            "endColumn" : 59
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "ded4994b8d85f4a:1",
        "primaryLocationStartColumnFingerprint" : "11"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/wrappers/local_cli_wrapper.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 12
          },
          "region" : {
            "startLine" : 87,
            "startColumn" : 25,
            "endColumn" : 66
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "cfb40158f337fd39:1",
        "primaryLocationStartColumnFingerprint" : "18"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/wrappers/local_cli_wrapper_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 13
          },
          "region" : {
            "startLine" : 142,
            "startColumn" : 21,
            "endColumn" : 38
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "84ea43aacba6043f:1",
        "primaryLocationStartColumnFingerprint" : "16"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/kernel_tests/logging_ops_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 14
          },
          "region" : {
            "startLine" : 311,
            "startColumn" : 20,
            "endColumn" : 52
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "a1321b967268c3cb:1",
        "primaryLocationStartColumnFingerprint" : "15"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/cli/readline_ui_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 15
          },
          "region" : {
            "startLine" : 40,
            "startColumn" : 54,
            "endColumn" : 71
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "bc4375439b65dca9:1",
        "primaryLocationStartColumnFingerprint" : "45"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/cli/readline_ui_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 15
          },
          "region" : {
            "startLine" : 171,
            "startColumn" : 19,
            "endColumn" : 36
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "56a744e8b6c586f2:1",
        "primaryLocationStartColumnFingerprint" : "14"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/debug/lib/source_utils_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 16
          },
          "region" : {
            "startLine" : 211,
            "startColumn" : 29,
            "endColumn" : 46
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "e02a5e99ba6fad87:1",
        "primaryLocationStartColumnFingerprint" : "24"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/framework/test_util.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 17
          },
          "region" : {
            "startLine" : 1833,
            "startColumn" : 21,
            "endColumn" : 61
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "b733ac2934c602de:1",
        "primaryLocationStartColumnFingerprint" : "16"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/lite/schema/upgrade_schema_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 18
          },
          "region" : {
            "startLine" : 257,
            "startColumn" : 20,
            "endColumn" : 51
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "c535bc3e75e28706:1",
        "primaryLocationStartColumnFingerprint" : "15"
      }
    }, {
      "ruleId" : "py/insecure-temporary-file",
      "ruleIndex" : 24,
      "rule" : {
        "id" : "py/insecure-temporary-file",
        "index" : 24
      },
      "message" : {
        "text" : "Call to deprecated function tempfile.mktemp may be insecure."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/lite/schema/upgrade_schema_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 18
          },
          "region" : {
            "startLine" : 263,
            "startColumn" : 25,
            "endColumn" : 55
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "d9d17bdecd072703:1",
        "primaryLocationStartColumnFingerprint" : "20"
      }
    }, {
      "ruleId" : "py/tarslip",
      "ruleIndex" : 35,
      "rule" : {
        "id" : "py/tarslip",
        "index" : 35
      },
      "message" : {
        "text" : "This file extraction depends on a [potentially untrusted source](1)."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/contrib/model_pruning/examples/cifar10/cifar10_pruning.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 19
          },
          "region" : {
            "startLine" : 403,
            "startColumn" : 3,
            "endColumn" : 33
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "3ae903ed8f31d898:1",
        "primaryLocationStartColumnFingerprint" : "0"
      },
      "relatedLocations" : [ {
        "id" : 1,
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/contrib/model_pruning/examples/cifar10/cifar10_pruning.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 19
          },
          "region" : {
            "startLine" : 403,
            "startColumn" : 3,
            "endColumn" : 33
          }
        },
        "message" : {
          "text" : "potentially untrusted source"
        }
      } ]
    }, {
      "ruleId" : "py/tarslip",
      "ruleIndex" : 35,
      "rule" : {
        "id" : "py/tarslip",
        "index" : 35
      },
      "message" : {
        "text" : "This file extraction depends on a [potentially untrusted source](1)."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/contrib/eager/python/examples/revnet/cifar_tfrecords.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 20
          },
          "region" : {
            "startLine" : 51,
            "startColumn" : 3,
            "endColumn" : 47
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "4b639abaf36d2ebe:1",
        "primaryLocationStartColumnFingerprint" : "0"
      },
      "relatedLocations" : [ {
        "id" : 1,
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/contrib/eager/python/examples/revnet/cifar_tfrecords.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 20
          },
          "region" : {
            "startLine" : 51,
            "startColumn" : 3,
            "endColumn" : 47
          }
        },
        "message" : {
          "text" : "potentially untrusted source"
        }
      } ]
    }, {
      "ruleId" : "py/tarslip",
      "ruleIndex" : 35,
      "rule" : {
        "id" : "py/tarslip",
        "index" : 35
      },
      "message" : {
        "text" : "This file extraction depends on a [potentially untrusted source](1).\nThis file extraction depends on a [potentially untrusted source](1)."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/keras/utils/data_utils.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 21
          },
          "region" : {
            "startLine" : 138,
            "startColumn" : 11,
            "endColumn" : 18
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "aaa1adc905323a16:1",
        "primaryLocationStartColumnFingerprint" : "0"
      },
      "codeFlows" : [ {
        "threadFlows" : [ {
          "locations" : [ {
            "location" : {
              "physicalLocation" : {
                "artifactLocation" : {
                  "uri" : "tensorflow/python/keras/utils/data_utils.py",
                  "uriBaseId" : "%SRCROOT%",
                  "index" : 21
                },
                "region" : {
                  "startLine" : 136,
                  "startColumn" : 12,
                  "endColumn" : 30
                }
              },
              "message" : {
                "text" : "ControlFlowNode for open_fn()"
              }
            }
          }, {
            "location" : {
              "physicalLocation" : {
                "artifactLocation" : {
                  "uri" : "tensorflow/python/keras/utils/data_utils.py",
                  "uriBaseId" : "%SRCROOT%",
                  "index" : 21
                },
                "region" : {
                  "startLine" : 136,
                  "startColumn" : 34,
                  "endColumn" : 41
                }
              },
              "message" : {
                "text" : "ControlFlowNode for archive"
              }
            }
          }, {
            "location" : {
              "physicalLocation" : {
                "artifactLocation" : {
                  "uri" : "tensorflow/python/keras/utils/data_utils.py",
                  "uriBaseId" : "%SRCROOT%",
                  "index" : 21
                },
                "region" : {
                  "startLine" : 138,
                  "startColumn" : 11,
                  "endColumn" : 18
                }
              },
              "message" : {
                "text" : "ControlFlowNode for archive"
              }
            }
          } ]
        } ]
      }, {
        "threadFlows" : [ {
          "locations" : [ {
            "location" : {
              "physicalLocation" : {
                "artifactLocation" : {
                  "uri" : "tensorflow/python/keras/utils/data_utils.py",
                  "uriBaseId" : "%SRCROOT%",
                  "index" : 21
                },
                "region" : {
                  "startLine" : 136,
                  "startColumn" : 12,
                  "endColumn" : 30
                }
              },
              "message" : {
                "text" : "ControlFlowNode for open_fn()"
              }
            }
          }, {
            "location" : {
              "physicalLocation" : {
                "artifactLocation" : {
                  "uri" : "tensorflow/python/keras/utils/data_utils.py",
                  "uriBaseId" : "%SRCROOT%",
                  "index" : 21
                },
                "region" : {
                  "startLine" : 136,
                  "startColumn" : 34,
                  "endColumn" : 41
                }
              },
              "message" : {
                "text" : "ControlFlowNode for archive"
              }
            }
          }, {
            "location" : {
              "physicalLocation" : {
                "artifactLocation" : {
                  "uri" : "tensorflow/python/keras/utils/data_utils.py",
                  "uriBaseId" : "%SRCROOT%",
                  "index" : 21
                },
                "region" : {
                  "startLine" : 138,
                  "startColumn" : 11,
                  "endColumn" : 18
                }
              },
              "message" : {
                "text" : "ControlFlowNode for archive"
              }
            }
          } ]
        } ]
      } ],
      "relatedLocations" : [ {
        "id" : 1,
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/keras/utils/data_utils.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 21
          },
          "region" : {
            "startLine" : 136,
            "startColumn" : 12,
            "endColumn" : 30
          }
        },
        "message" : {
          "text" : "potentially untrusted source"
        }
      } ]
    }, {
      "ruleId" : "py/tarslip",
      "ruleIndex" : 35,
      "rule" : {
        "id" : "py/tarslip",
        "index" : 35
      },
      "message" : {
        "text" : "This file extraction depends on a [potentially untrusted source](1)."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/examples/speech_commands/input_data.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 22
          },
          "region" : {
            "startLine" : 243,
            "startColumn" : 7,
            "endColumn" : 37
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "71b2af8c91b5277e:1",
        "primaryLocationStartColumnFingerprint" : "0"
      },
      "relatedLocations" : [ {
        "id" : 1,
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/examples/speech_commands/input_data.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 22
          },
          "region" : {
            "startLine" : 243,
            "startColumn" : 7,
            "endColumn" : 37
          }
        },
        "message" : {
          "text" : "potentially untrusted source"
        }
      } ]
    }, {
      "ruleId" : "py/tarslip",
      "ruleIndex" : 35,
      "rule" : {
        "id" : "py/tarslip",
        "index" : 35
      },
      "message" : {
        "text" : "This file extraction depends on a [potentially untrusted source](1)."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/contrib/learn/python/learn/datasets/text_datasets.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 23
          },
          "region" : {
            "startLine" : 48,
            "startColumn" : 5,
            "endColumn" : 10
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "c5c560d62f5590a8:1",
        "primaryLocationStartColumnFingerprint" : "0"
      },
      "codeFlows" : [ {
        "threadFlows" : [ {
          "locations" : [ {
            "location" : {
              "physicalLocation" : {
                "artifactLocation" : {
                  "uri" : "tensorflow/contrib/learn/python/learn/datasets/text_datasets.py",
                  "uriBaseId" : "%SRCROOT%",
                  "index" : 23
                },
                "region" : {
                  "startLine" : 47,
                  "startColumn" : 13,
                  "endColumn" : 46
                }
              },
              "message" : {
                "text" : "ControlFlowNode for Attribute()"
              }
            }
          }, {
            "location" : {
              "physicalLocation" : {
                "artifactLocation" : {
                  "uri" : "tensorflow/contrib/learn/python/learn/datasets/text_datasets.py",
                  "uriBaseId" : "%SRCROOT%",
                  "index" : 23
                },
                "region" : {
                  "startLine" : 47,
                  "startColumn" : 5,
                  "endColumn" : 10
                }
              },
              "message" : {
                "text" : "ControlFlowNode for tfile"
              }
            }
          }, {
            "location" : {
              "physicalLocation" : {
                "artifactLocation" : {
                  "uri" : "tensorflow/contrib/learn/python/learn/datasets/text_datasets.py",
                  "uriBaseId" : "%SRCROOT%",
                  "index" : 23
                },
                "region" : {
                  "startLine" : 48,
                  "startColumn" : 5,
                  "endColumn" : 10
                }
              },
              "message" : {
                "text" : "ControlFlowNode for tfile"
              }
            }
          } ]
        } ]
      } ],
      "relatedLocations" : [ {
        "id" : 1,
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/contrib/learn/python/learn/datasets/text_datasets.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 23
          },
          "region" : {
            "startLine" : 47,
            "startColumn" : 13,
            "endColumn" : 46
          }
        },
        "message" : {
          "text" : "potentially untrusted source"
        }
      } ]
    }, {
      "ruleId" : "py/overly-permissive-file",
      "ruleIndex" : 40,
      "rule" : {
        "id" : "py/overly-permissive-file",
        "index" : 40
      },
      "message" : {
        "text" : "Overly permissive mask in chmod sets file to world writable."
      },
      "locations" : [ {
        "physicalLocation" : {
          "artifactLocation" : {
            "uri" : "tensorflow/python/lib/io/file_io_test.py",
            "uriBaseId" : "%SRCROOT%",
            "index" : 24
          },
          "region" : {
            "startLine" : 609,
            "startColumn" : 5,
            "endColumn" : 33
          }
        }
      } ],
      "partialFingerprints" : {
        "primaryLocationLineHash" : "d451331f1f6ae537:1",
        "primaryLocationStartColumnFingerprint" : "0"
      }
    } ]
}

# Flattening JSON data
flattened_data = []
for result in data['results']:
    base_data = {
        'ruleId': result['ruleId'],
        'ruleIndex': result['ruleIndex'],
        'message_text': result['message']['text']
    }
    for location in result['locations']:
        loc_data = base_data.copy()
        loc_data.update({
            'uri': location['physicalLocation']['artifactLocation']['uri'],
            'uriBaseId': location['physicalLocation']['artifactLocation']['uriBaseId'],
            'index': location['physicalLocation']['artifactLocation']['index'],
            'startLine': location['physicalLocation']['region']['startLine'],
            'startColumn': location['physicalLocation']['region']['startColumn'],
            'endColumn': location['physicalLocation']['region']['endColumn']
        })
        flattened_data.append(loc_data)

# Creating DataFrame
df = pd.DataFrame(flattened_data)

# Saving to CSV
csv_file = 'results5.csv'
df.to_csv(csv_file, index=False)

