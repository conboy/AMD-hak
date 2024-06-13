import pandas as pd
import json

# Sample JSON data
json_data = {
    "rules" : [ {
          "id" : "py/use-of-input",
          "name" : "py/use-of-input",
          "shortDescription" : {
            "text" : "'input' function used in Python 2"
          },
          "fullDescription" : {
            "text" : "The built-in function 'input' is used which, in Python 2, can allow arbitrary code to be run."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "correctness", "security/cwe/cwe-94", "security/cwe/cwe-95" ],
            "description" : "The built-in function 'input' is used which, in Python 2, can allow arbitrary code to be run.",
            "id" : "py/use-of-input",
            "kind" : "problem",
            "name" : "'input' function used in Python 2",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "9.8",
            "sub-severity" : "high"
          }
        }, {
          "id" : "py/bind-socket-all-network-interfaces",
          "name" : "py/bind-socket-all-network-interfaces",
          "shortDescription" : {
            "text" : "Binding a socket to all network interfaces"
          },
          "fullDescription" : {
            "text" : "Binding a socket to all interfaces opens it up to traffic from any IPv4 address and is therefore associated with security risks."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-200" ],
            "description" : "Binding a socket to all interfaces opens it up to traffic from any IPv4 address\n and is therefore associated with security risks.",
            "id" : "py/bind-socket-all-network-interfaces",
            "kind" : "problem",
            "name" : "Binding a socket to all network interfaces",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "6.5",
            "sub-severity" : "low"
          }
        }, {
          "id" : "py/incomplete-hostname-regexp",
          "name" : "py/incomplete-hostname-regexp",
          "shortDescription" : {
            "text" : "Incomplete regular expression for hostnames"
          },
          "fullDescription" : {
            "text" : "Matching a URL or hostname against a regular expression that contains an unescaped dot as part of the hostname might match more hostnames than expected."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "correctness", "security", "external/cwe/cwe-020" ],
            "description" : "Matching a URL or hostname against a regular expression that contains an unescaped dot as part of the hostname might match more hostnames than expected.",
            "id" : "py/incomplete-hostname-regexp",
            "kind" : "problem",
            "name" : "Incomplete regular expression for hostnames",
            "precision" : "high",
            "problem.severity" : "warning",
            "security-severity" : "7.8"
          }
        }, {
          "id" : "py/incomplete-url-substring-sanitization",
          "name" : "py/incomplete-url-substring-sanitization",
          "shortDescription" : {
            "text" : "Incomplete URL substring sanitization"
          },
          "fullDescription" : {
            "text" : "Security checks on the substrings of an unparsed URL are often vulnerable to bypassing."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "correctness", "security", "external/cwe/cwe-20" ],
            "description" : "Security checks on the substrings of an unparsed URL are often vulnerable to bypassing.",
            "id" : "py/incomplete-url-substring-sanitization",
            "kind" : "problem",
            "name" : "Incomplete URL substring sanitization",
            "precision" : "high",
            "problem.severity" : "warning",
            "security-severity" : "7.8"
          }
        }, {
          "id" : "py/overly-large-range",
          "name" : "py/overly-large-range",
          "shortDescription" : {
            "text" : "Overly permissive regular expression range"
          },
          "fullDescription" : {
            "text" : "Overly permissive regular expression ranges match a wider range of characters than intended. This may allow an attacker to bypass a filter or sanitizer."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "correctness", "security", "external/cwe/cwe-020" ],
            "description" : "Overly permissive regular expression ranges match a wider range of characters than intended.\n              This may allow an attacker to bypass a filter or sanitizer.",
            "id" : "py/overly-large-range",
            "kind" : "problem",
            "name" : "Overly permissive regular expression range",
            "precision" : "high",
            "problem.severity" : "warning",
            "security-severity" : "5.0"
          }
        }, {
          "id" : "py/path-injection",
          "name" : "py/path-injection",
          "shortDescription" : {
            "text" : "Uncontrolled data used in path expression"
          },
          "fullDescription" : {
            "text" : "Accessing paths influenced by users can allow an attacker to access unexpected resources."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "correctness", "security", "external/cwe/cwe-022", "external/cwe/cwe-023", "external/cwe/cwe-036", "external/cwe/cwe-073", "external/cwe/cwe-099" ],
            "description" : "Accessing paths influenced by users can allow an attacker to access unexpected resources.",
            "id" : "py/path-injection",
            "kind" : "path-problem",
            "name" : "Uncontrolled data used in path expression",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "7.5",
            "sub-severity" : "high"
          }
        }, {
          "id" : "py/command-line-injection",
          "name" : "py/command-line-injection",
          "shortDescription" : {
            "text" : "Uncontrolled command line"
          },
          "fullDescription" : {
            "text" : "Using externally controlled strings in a command line may allow a malicious user to change the meaning of the command."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "correctness", "security", "external/cwe/cwe-078", "external/cwe/cwe-088" ],
            "description" : "Using externally controlled strings in a command line may allow a malicious\n              user to change the meaning of the command.",
            "id" : "py/command-line-injection",
            "kind" : "path-problem",
            "name" : "Uncontrolled command line",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "9.8",
            "sub-severity" : "high"
          }
        }, {
          "id" : "py/reflective-xss",
          "name" : "py/reflective-xss",
          "shortDescription" : {
            "text" : "Reflected server-side cross-site scripting"
          },
          "fullDescription" : {
            "text" : "Writing user input directly to a web page allows for a cross-site scripting vulnerability."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-079", "external/cwe/cwe-116" ],
            "description" : "Writing user input directly to a web page\n              allows for a cross-site scripting vulnerability.",
            "id" : "py/reflective-xss",
            "kind" : "path-problem",
            "name" : "Reflected server-side cross-site scripting",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "6.1",
            "sub-severity" : "high"
          }
        }, {
          "id" : "py/sql-injection",
          "name" : "py/sql-injection",
          "shortDescription" : {
            "text" : "SQL query built from user-controlled sources"
          },
          "fullDescription" : {
            "text" : "Building a SQL query from user-controlled sources is vulnerable to insertion of malicious SQL code by the user."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-089" ],
            "description" : "Building a SQL query from user-controlled sources is vulnerable to insertion of\n              malicious SQL code by the user.",
            "id" : "py/sql-injection",
            "kind" : "path-problem",
            "name" : "SQL query built from user-controlled sources",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "8.8"
          }
        }, {
          "id" : "py/ldap-injection",
          "name" : "py/ldap-injection",
          "shortDescription" : {
            "text" : "LDAP query built from user-controlled sources"
          },
          "fullDescription" : {
            "text" : "Building an LDAP query from user-controlled sources is vulnerable to insertion of malicious LDAP code by the user."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-090" ],
            "description" : "Building an LDAP query from user-controlled sources is vulnerable to insertion of\n              malicious LDAP code by the user.",
            "id" : "py/ldap-injection",
            "kind" : "path-problem",
            "name" : "LDAP query built from user-controlled sources",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "9.8"
          }
        }, {
          "id" : "py/code-injection",
          "name" : "py/code-injection",
          "shortDescription" : {
            "text" : "Code injection"
          },
          "fullDescription" : {
            "text" : "Interpreting unsanitized user input as code allows a malicious user to perform arbitrary code execution."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-094", "external/cwe/cwe-095", "external/cwe/cwe-116" ],
            "description" : "Interpreting unsanitized user input as code allows a malicious user to perform arbitrary\n              code execution.",
            "id" : "py/code-injection",
            "kind" : "path-problem",
            "name" : "Code injection",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "9.3",
            "sub-severity" : "high"
          }
        }, {
          "id" : "py/bad-tag-filter",
          "name" : "py/bad-tag-filter",
          "shortDescription" : {
            "text" : "Bad HTML filtering regexp"
          },
          "fullDescription" : {
            "text" : "Matching HTML tags using regular expressions is hard to do right, and can easily lead to security issues."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "correctness", "security", "external/cwe/cwe-116", "external/cwe/cwe-020", "external/cwe/cwe-185", "external/cwe/cwe-186" ],
            "description" : "Matching HTML tags using regular expressions is hard to do right, and can easily lead to security issues.",
            "id" : "py/bad-tag-filter",
            "kind" : "problem",
            "name" : "Bad HTML filtering regexp",
            "precision" : "high",
            "problem.severity" : "warning",
            "security-severity" : "7.8"
          }
        }, {
          "id" : "py/stack-trace-exposure",
          "name" : "py/stack-trace-exposure",
          "shortDescription" : {
            "text" : "Information exposure through an exception"
          },
          "fullDescription" : {
            "text" : "Leaking information about an exception, such as messages and stack traces, to an external user can expose implementation details that are useful to an attacker for developing a subsequent exploit."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-209", "external/cwe/cwe-497" ],
            "description" : "Leaking information about an exception, such as messages and stack traces, to an\n              external user can expose implementation details that are useful to an attacker for\n              developing a subsequent exploit.",
            "id" : "py/stack-trace-exposure",
            "kind" : "path-problem",
            "name" : "Information exposure through an exception",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "5.4"
          }
        }, {
          "id" : "py/flask-debug",
          "name" : "py/flask-debug",
          "shortDescription" : {
            "text" : "Flask app is run in debug mode"
          },
          "fullDescription" : {
            "text" : "Running a Flask app in debug mode may allow an attacker to run arbitrary code through the Werkzeug debugger."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-215", "external/cwe/cwe-489" ],
            "description" : "Running a Flask app in debug mode may allow an attacker to run arbitrary code through the Werkzeug debugger.",
            "id" : "py/flask-debug",
            "kind" : "problem",
            "name" : "Flask app is run in debug mode",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/pam-auth-bypass",
          "name" : "py/pam-auth-bypass",
          "shortDescription" : {
            "text" : "PAM authorization bypass due to incorrect usage"
          },
          "fullDescription" : {
            "text" : "Not using `pam_acct_mgmt` after `pam_authenticate` to check the validity of a login can lead to authorization bypass."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-285" ],
            "description" : "Not using `pam_acct_mgmt` after `pam_authenticate` to check the validity of a login can lead to authorization bypass.",
            "id" : "py/pam-auth-bypass",
            "kind" : "path-problem",
            "name" : "PAM authorization bypass due to incorrect usage",
            "precision" : "high",
            "problem.severity" : "warning",
            "security-severity" : "8.1"
          }
        }, {
          "id" : "py/paramiko-missing-host-key-validation",
          "name" : "py/paramiko-missing-host-key-validation",
          "shortDescription" : {
            "text" : "Accepting unknown SSH host keys when using Paramiko"
          },
          "fullDescription" : {
            "text" : "Accepting unknown host keys can allow man-in-the-middle attacks."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-295" ],
            "description" : "Accepting unknown host keys can allow man-in-the-middle attacks.",
            "id" : "py/paramiko-missing-host-key-validation",
            "kind" : "problem",
            "name" : "Accepting unknown SSH host keys when using Paramiko",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/clear-text-logging-sensitive-data",
          "name" : "py/clear-text-logging-sensitive-data",
          "shortDescription" : {
            "text" : "Clear-text logging of sensitive information"
          },
          "fullDescription" : {
            "text" : "Logging sensitive information without encryption or hashing can expose it to an attacker."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-312", "external/cwe/cwe-359", "external/cwe/cwe-532" ],
            "description" : "Logging sensitive information without encryption or hashing can\n              expose it to an attacker.",
            "id" : "py/clear-text-logging-sensitive-data",
            "kind" : "path-problem",
            "name" : "Clear-text logging of sensitive information",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/clear-text-storage-sensitive-data",
          "name" : "py/clear-text-storage-sensitive-data",
          "shortDescription" : {
            "text" : "Clear-text storage of sensitive information"
          },
          "fullDescription" : {
            "text" : "Sensitive information stored without encryption or hashing can expose it to an attacker."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-312", "external/cwe/cwe-315", "external/cwe/cwe-359" ],
            "description" : "Sensitive information stored without encryption or hashing can expose it to an\n              attacker.",
            "id" : "py/clear-text-storage-sensitive-data",
            "kind" : "path-problem",
            "name" : "Clear-text storage of sensitive information",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/weak-crypto-key",
          "name" : "py/weak-crypto-key",
          "shortDescription" : {
            "text" : "Use of weak cryptographic key"
          },
          "fullDescription" : {
            "text" : "Use of a cryptographic key that is too small may allow the encryption to be broken."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-326" ],
            "description" : "Use of a cryptographic key that is too small may allow the encryption to be broken.",
            "id" : "py/weak-crypto-key",
            "kind" : "problem",
            "name" : "Use of weak cryptographic key",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/weak-cryptographic-algorithm",
          "name" : "py/weak-cryptographic-algorithm",
          "shortDescription" : {
            "text" : "Use of a broken or weak cryptographic algorithm"
          },
          "fullDescription" : {
            "text" : "Using broken or weak cryptographic algorithms can compromise security."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-327" ],
            "description" : "Using broken or weak cryptographic algorithms can compromise security.",
            "id" : "py/weak-cryptographic-algorithm",
            "kind" : "problem",
            "name" : "Use of a broken or weak cryptographic algorithm",
            "precision" : "high",
            "problem.severity" : "warning",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/insecure-default-protocol",
          "name" : "py/insecure-default-protocol",
          "shortDescription" : {
            "text" : "Default version of SSL/TLS may be insecure"
          },
          "fullDescription" : {
            "text" : "Leaving the SSL/TLS version unspecified may result in an insecure default protocol being used."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-327" ],
            "description" : "Leaving the SSL/TLS version unspecified may result in an insecure\n              default protocol being used.",
            "id" : "py/insecure-default-protocol",
            "kind" : "problem",
            "name" : "Default version of SSL/TLS may be insecure",
            "precision" : "high",
            "problem.severity" : "warning",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/insecure-protocol",
          "name" : "py/insecure-protocol",
          "shortDescription" : {
            "text" : "Use of insecure SSL/TLS version"
          },
          "fullDescription" : {
            "text" : "Using an insecure SSL/TLS version may leave the connection vulnerable to attacks."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-327" ],
            "description" : "Using an insecure SSL/TLS version may leave the connection vulnerable to attacks.",
            "id" : "py/insecure-protocol",
            "kind" : "problem",
            "name" : "Use of insecure SSL/TLS version",
            "precision" : "high",
            "problem.severity" : "warning",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/weak-sensitive-data-hashing",
          "name" : "py/weak-sensitive-data-hashing",
          "shortDescription" : {
            "text" : "Use of a broken or weak cryptographic hashing algorithm on sensitive data"
          },
          "fullDescription" : {
            "text" : "Using broken or weak cryptographic hashing algorithms can compromise security."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-327", "external/cwe/cwe-328", "external/cwe/cwe-916" ],
            "description" : "Using broken or weak cryptographic hashing algorithms can compromise security.",
            "id" : "py/weak-sensitive-data-hashing",
            "kind" : "path-problem",
            "name" : "Use of a broken or weak cryptographic hashing algorithm on sensitive data",
            "precision" : "high",
            "problem.severity" : "warning",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/csrf-protection-disabled",
          "name" : "py/csrf-protection-disabled",
          "shortDescription" : {
            "text" : "CSRF protection weakened or disabled"
          },
          "fullDescription" : {
            "text" : "Disabling or weakening CSRF protection may make the application vulnerable to a Cross-Site Request Forgery (CSRF) attack."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-352" ],
            "description" : "Disabling or weakening CSRF protection may make the application\n              vulnerable to a Cross-Site Request Forgery (CSRF) attack.",
            "id" : "py/csrf-protection-disabled",
            "kind" : "problem",
            "name" : "CSRF protection weakened or disabled",
            "precision" : "high",
            "problem.severity" : "warning",
            "security-severity" : "8.8"
          }
        }, {
          "id" : "py/insecure-temporary-file",
          "name" : "py/insecure-temporary-file",
          "shortDescription" : {
            "text" : "Insecure temporary file"
          },
          "fullDescription" : {
            "text" : "Creating a temporary file using this method may be insecure."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "external/cwe/cwe-377", "security" ],
            "description" : "Creating a temporary file using this method may be insecure.",
            "id" : "py/insecure-temporary-file",
            "kind" : "problem",
            "name" : "Insecure temporary file",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "7.0",
            "sub-severity" : "high"
          }
        }, {
          "id" : "py/unsafe-deserialization",
          "name" : "py/unsafe-deserialization",
          "shortDescription" : {
            "text" : "Deserialization of user-controlled data"
          },
          "fullDescription" : {
            "text" : "Deserializing user-controlled data may allow attackers to execute arbitrary code."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "external/cwe/cwe-502", "security", "serialization" ],
            "description" : "Deserializing user-controlled data may allow attackers to execute arbitrary code.",
            "id" : "py/unsafe-deserialization",
            "kind" : "path-problem",
            "name" : "Deserialization of user-controlled data",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "9.8",
            "sub-severity" : "high"
          }
        }, {
          "id" : "py/url-redirection",
          "name" : "py/url-redirection",
          "shortDescription" : {
            "text" : "URL redirection from remote source"
          },
          "fullDescription" : {
            "text" : "URL redirection based on unvalidated user input may cause redirection to malicious web sites."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-601" ],
            "description" : "URL redirection based on unvalidated user input\n              may cause redirection to malicious web sites.",
            "id" : "py/url-redirection",
            "kind" : "path-problem",
            "name" : "URL redirection from remote source",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "6.1",
            "sub-severity" : "low"
          }
        }, {
          "id" : "py/xxe",
          "name" : "py/xxe",
          "shortDescription" : {
            "text" : "XML external entity expansion"
          },
          "fullDescription" : {
            "text" : "Parsing user input as an XML document with external entity expansion is vulnerable to XXE attacks."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-611", "external/cwe/cwe-827" ],
            "description" : "Parsing user input as an XML document with external\n              entity expansion is vulnerable to XXE attacks.",
            "id" : "py/xxe",
            "kind" : "path-problem",
            "name" : "XML external entity expansion",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "9.1"
          }
        }, {
          "id" : "py/xpath-injection",
          "name" : "py/xpath-injection",
          "shortDescription" : {
            "text" : "XPath query built from user-controlled sources"
          },
          "fullDescription" : {
            "text" : "Building a XPath query from user-controlled sources is vulnerable to insertion of malicious Xpath code by the user."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-643" ],
            "description" : "Building a XPath query from user-controlled sources is vulnerable to insertion of\n              malicious Xpath code by the user.",
            "id" : "py/xpath-injection",
            "kind" : "path-problem",
            "name" : "XPath query built from user-controlled sources",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "9.8"
          }
        }, {
          "id" : "py/polynomial-redos",
          "name" : "py/polynomial-redos",
          "shortDescription" : {
            "text" : "Polynomial regular expression used on uncontrolled data"
          },
          "fullDescription" : {
            "text" : "A regular expression that can require polynomial time to match may be vulnerable to denial-of-service attacks."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-1333", "external/cwe/cwe-730", "external/cwe/cwe-400" ],
            "description" : "A regular expression that can require polynomial time\n              to match may be vulnerable to denial-of-service attacks.",
            "id" : "py/polynomial-redos",
            "kind" : "path-problem",
            "name" : "Polynomial regular expression used on uncontrolled data",
            "precision" : "high",
            "problem.severity" : "warning",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/redos",
          "name" : "py/redos",
          "shortDescription" : {
            "text" : "Inefficient regular expression"
          },
          "fullDescription" : {
            "text" : "A regular expression that requires exponential time to match certain inputs can be a performance bottleneck, and may be vulnerable to denial-of-service attacks."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-1333", "external/cwe/cwe-730", "external/cwe/cwe-400" ],
            "description" : "A regular expression that requires exponential time to match certain inputs\n              can be a performance bottleneck, and may be vulnerable to denial-of-service\n              attacks.",
            "id" : "py/redos",
            "kind" : "problem",
            "name" : "Inefficient regular expression",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/regex-injection",
          "name" : "py/regex-injection",
          "shortDescription" : {
            "text" : "Regular expression injection"
          },
          "fullDescription" : {
            "text" : "User input should not be used in regular expressions without first being escaped, otherwise a malicious user may be able to inject an expression that could require exponential time on certain inputs."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-730", "external/cwe/cwe-400" ],
            "description" : "User input should not be used in regular expressions without first being escaped,\n              otherwise a malicious user may be able to inject an expression that could require\n              exponential time on certain inputs.",
            "id" : "py/regex-injection",
            "kind" : "path-problem",
            "name" : "Regular expression injection",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/xml-bomb",
          "name" : "py/xml-bomb",
          "shortDescription" : {
            "text" : "XML internal entity expansion"
          },
          "fullDescription" : {
            "text" : "Parsing user input as an XML document with arbitrary internal entity expansion is vulnerable to denial-of-service attacks."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-776", "external/cwe/cwe-400" ],
            "description" : "Parsing user input as an XML document with arbitrary internal\n              entity expansion is vulnerable to denial-of-service attacks.",
            "id" : "py/xml-bomb",
            "kind" : "path-problem",
            "name" : "XML internal entity expansion",
            "precision" : "high",
            "problem.severity" : "warning",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/full-ssrf",
          "name" : "py/full-ssrf",
          "shortDescription" : {
            "text" : "Full server-side request forgery"
          },
          "fullDescription" : {
            "text" : "Making a network request to a URL that is fully user-controlled allows for request forgery attacks."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-918" ],
            "description" : "Making a network request to a URL that is fully user-controlled allows for request forgery attacks.",
            "id" : "py/full-ssrf",
            "kind" : "path-problem",
            "name" : "Full server-side request forgery",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "9.1"
          }
        }, {
          "id" : "py/nosql-injection",
          "name" : "py/nosql-injection",
          "shortDescription" : {
            "text" : "NoSQL Injection"
          },
          "fullDescription" : {
            "text" : "Building a NoSQL query from user-controlled sources is vulnerable to insertion of malicious NoSQL code by the user."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-943" ],
            "description" : "Building a NoSQL query from user-controlled sources is vulnerable to insertion of\n              malicious NoSQL code by the user.",
            "id" : "py/nosql-injection",
            "kind" : "path-problem",
            "name" : "NoSQL Injection",
            "precision" : "high",
            "problem.severity" : "error",
            "security-severity" : "8.8"
          }
        }, {
          "id" : "py/tarslip",
          "name" : "py/tarslip",
          "shortDescription" : {
            "text" : "Arbitrary file write during tarfile extraction"
          },
          "fullDescription" : {
            "text" : "Extracting files from a malicious tar archive without validating that the destination file path is within the destination directory can cause files outside the destination directory to be overwritten."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-022" ],
            "description" : "Extracting files from a malicious tar archive without validating that the\n              destination file path is within the destination directory can cause files outside\n              the destination directory to be overwritten.",
            "id" : "py/tarslip",
            "kind" : "path-problem",
            "name" : "Arbitrary file write during tarfile extraction",
            "precision" : "medium",
            "problem.severity" : "error",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/shell-command-constructed-from-input",
          "name" : "py/shell-command-constructed-from-input",
          "shortDescription" : {
            "text" : "Unsafe shell command constructed from library input"
          },
          "fullDescription" : {
            "text" : "Using externally controlled strings in a command line may allow a malicious user to change the meaning of the command."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "correctness", "security", "external/cwe/cwe-078", "external/cwe/cwe-088", "external/cwe/cwe-073" ],
            "description" : "Using externally controlled strings in a command line may allow a malicious\n              user to change the meaning of the command.",
            "id" : "py/shell-command-constructed-from-input",
            "kind" : "path-problem",
            "name" : "Unsafe shell command constructed from library input",
            "precision" : "medium",
            "problem.severity" : "error",
            "security-severity" : "6.3"
          }
        }, {
          "id" : "py/jinja2/autoescape-false",
          "name" : "py/jinja2/autoescape-false",
          "shortDescription" : {
            "text" : "Jinja2 templating with autoescape=False"
          },
          "fullDescription" : {
            "text" : "Using jinja2 templates with 'autoescape=False' can cause a cross-site scripting vulnerability."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-079" ],
            "description" : "Using jinja2 templates with 'autoescape=False' can\n              cause a cross-site scripting vulnerability.",
            "id" : "py/jinja2/autoescape-false",
            "kind" : "problem",
            "name" : "Jinja2 templating with autoescape=False",
            "precision" : "medium",
            "problem.severity" : "error",
            "security-severity" : "6.1"
          }
        }, {
          "id" : "py/log-injection",
          "name" : "py/log-injection",
          "shortDescription" : {
            "text" : "Log Injection"
          },
          "fullDescription" : {
            "text" : "Building log entries from user-controlled data is vulnerable to insertion of forged log entries by a malicious user."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-117" ],
            "description" : "Building log entries from user-controlled data is vulnerable to\n              insertion of forged log entries by a malicious user.",
            "id" : "py/log-injection",
            "kind" : "path-problem",
            "name" : "Log Injection",
            "precision" : "medium",
            "problem.severity" : "error",
            "security-severity" : "7.8"
          }
        }, {
          "id" : "py/request-without-cert-validation",
          "name" : "py/request-without-cert-validation",
          "shortDescription" : {
            "text" : "Request without certificate validation"
          },
          "fullDescription" : {
            "text" : "Making a request without certificate validation can allow man-in-the-middle attacks."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-295" ],
            "description" : "Making a request without certificate validation can allow man-in-the-middle attacks.",
            "id" : "py/request-without-cert-validation",
            "kind" : "problem",
            "name" : "Request without certificate validation",
            "precision" : "medium",
            "problem.severity" : "error",
            "security-severity" : "7.5"
          }
        }, {
          "id" : "py/overly-permissive-file",
          "name" : "py/overly-permissive-file",
          "shortDescription" : {
            "text" : "Overly permissive file permissions"
          },
          "fullDescription" : {
            "text" : "Allowing files to be readable or writable by users other than the owner may allow sensitive information to be accessed."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "warning"
          },
          "properties" : {
            "tags" : [ "external/cwe/cwe-732", "security" ],
            "description" : "Allowing files to be readable or writable by users other than the owner may allow sensitive information to be accessed.",
            "id" : "py/overly-permissive-file",
            "kind" : "problem",
            "name" : "Overly permissive file permissions",
            "precision" : "medium",
            "problem.severity" : "warning",
            "security-severity" : "7.8",
            "sub-severity" : "high"
          }
        }, {
          "id" : "py/hardcoded-credentials",
          "name" : "py/hardcoded-credentials",
          "shortDescription" : {
            "text" : "Hard-coded credentials"
          },
          "fullDescription" : {
            "text" : "Credentials are hard coded in the source code of the application."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-259", "external/cwe/cwe-321", "external/cwe/cwe-798" ],
            "description" : "Credentials are hard coded in the source code of the application.",
            "id" : "py/hardcoded-credentials",
            "kind" : "path-problem",
            "name" : "Hard-coded credentials",
            "precision" : "medium",
            "problem.severity" : "error",
            "security-severity" : "9.8"
          }
        }, {
          "id" : "py/partial-ssrf",
          "name" : "py/partial-ssrf",
          "shortDescription" : {
            "text" : "Partial server-side request forgery"
          },
          "fullDescription" : {
            "text" : "Making a network request to a URL that is partially user-controlled allows for request forgery attacks."
          },
          "defaultConfiguration" : {
            "enabled" : "true",
            "level" : "error"
          },
          "properties" : {
            "tags" : [ "security", "external/cwe/cwe-918" ],
            "description" : "Making a network request to a URL that is partially user-controlled allows for request forgery attacks.",
            "id" : "py/partial-ssrf",
            "kind" : "path-problem",
            "name" : "Partial server-side request forgery",
            "precision" : "medium",
            "problem.severity" : "error",
            "security-severity" : "9.1"
          }
        }, {
          "id" : "py/summary/lines-of-code",
          "name" : "py/summary/lines-of-code",
          "shortDescription" : {
            "text" : "Total lines of Python code in the database"
          },
          "fullDescription" : {
            "text" : "The total number of lines of Python code across all files, including external libraries and auto-generated files. This is a useful metric of the size of a database. This query counts the lines of code, excluding whitespace or comments."
          },
          "defaultConfiguration" : {
            "enabled" : "true"
          },
          "properties" : {
            "tags" : [ "summary", "telemetry" ],
            "description" : "The total number of lines of Python code across all files, including\n   external libraries and auto-generated files. This is a useful metric of the size of a\n   database. This query counts the lines of code, excluding whitespace or comments.",
            "id" : "py/summary/lines-of-code",
            "kind" : "metric",
            "name" : "Total lines of Python code in the database"
          }
        }, {
          "id" : "py/summary/lines-of-user-code",
          "name" : "py/summary/lines-of-user-code",
          "shortDescription" : {
            "text" : "Total lines of user written Python code in the database"
          },
          "fullDescription" : {
            "text" : "The total number of lines of Python code from the source code directory, excluding auto-generated files. This query counts the lines of code, excluding whitespace or comments. Note: If external libraries are included in the codebase either in a checked-in virtual environment or as vendored code, that will currently be counted as user written code."
          },
          "defaultConfiguration" : {
            "enabled" : "true"
          },
          "properties" : {
            "tags" : [ "summary", "lines-of-code" ],
            "description" : "The total number of lines of Python code from the source code directory,\n   excluding auto-generated files. This query counts the lines of code, excluding\n   whitespace or comments. Note: If external libraries are included in the codebase\n   either in a checked-in virtual environment or as vendored code, that will currently\n   be counted as user written code.",
            "id" : "py/summary/lines-of-user-code",
            "kind" : "metric",
            "name" : "Total lines of user written Python code in the database"
          }
        } ]
}

# Function to flatten the JSON data
def flatten_json(json_data):
    rules = json_data["rules"]
    flattened_data = []

    for rule in rules:
        flattened_rule = {
            "id": rule.get("id"),
            "name": rule.get("name"),
            "shortDescription": rule.get("shortDescription", {}).get("text"),
            "fullDescription": rule.get("fullDescription", {}).get("text"),
            "enabled": rule.get("defaultConfiguration", {}).get("enabled"),
            "level": rule.get("defaultConfiguration", {}).get("level"),
            "tags": ', '.join(rule.get("properties", {}).get("tags", [])),
            "description": rule.get("properties", {}).get("description"),
            "kind": rule.get("properties", {}).get("kind"),
            "precision": rule.get("properties", {}).get("precision"),
            "problem.severity": rule.get("properties", {}).get("problem.severity"),
            "security-severity": rule.get("properties", {}).get("security-severity"),
            "sub-severity": rule.get("properties", {}).get("sub-severity")
        }
        flattened_data.append(flattened_rule)

    return flattened_data

# Flatten the JSON data
flattened_data = flatten_json(json_data)

# Convert to DataFrame
df = pd.DataFrame(flattened_data)

# Save to CSV
df.to_csv('flattened_rules.csv', index=False)

print("JSON data has been flattened and saved to 'flattened_rules.csv'")