# Cartuxeira
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://github.com/eliasgranderubio/cartuxeira)

**Cartuxeira** is a tool to perform an email risk evaluation relying on both offline and online black lists, machine learning techniques such as DGA detection or EGA detection, and using OSINT third party services.

This kind of email risk evaluation provides a confident way to identify a phishing attack without depending on user knowledge or awareness.

   * [Requirements](#requirements)
     * [Installation of MongoDB](#installation-of-mongodb)
   * [Usage](#usage)
     * [Local Black List Service](#local-black-list-service)
     * [Email Risk Evaluation Service](#email-risk-evaluation-service)
     * [Other REST API details](#other-rest-api-details)
       * [Version Prefix](#version-prefix)
       * [HTTP Status Codes](#http-status-codes)
   * [Bonus Track: Quick Start with Docker Compose](#bonus-track--quick-start-with-docker-compose)
   * [Bugs and Feedback](#bugs-and-feedback)


## Requirements
Before **Cartuxeira** usage, you must have installed the next requirements:

* Python 3.10.X or later
* MongoDB 6.0 or later
* Pip3
  * PyMongo
  * PyDNSBL
  * Flask
  * Waitress
  * Dgad
  * EmailRep

The requirements can be installed with pip:
```bash
    sudo pip3 install -r requirements.txt
```

### Installation of MongoDB
You must have installed MongoDB 6.0 or later for using **Cartuxeira**. MongoDB stores local black lists for both domains and emails and other relevant information.

If you need instructions for MongoDB installation, see the [How-to install MongoDB Community Edition](https://docs.mongodb.com/manual/administration/install-community/) page.

You can also run MongoDB using docker:
```bash
    docker pull mongo
    docker run -d -p 27017:27017 mongo
```

## Usage
You must run `python3 cartuxeira.py` for starting the **Cartuxeira** server. Type `python3 cartuxeira.py -h` for details about initial settings.

Once the server is up and running you can consume its REST API. The available API is shown below.


### Local Black List Service

**Cartuxeira** allows to manage a local black list for both domains and emails. For each one, you can add, remove or check if it is included or not in the black list.

The domain black list specification is shown below: 
<table style="width:100%"> 
  <tr>
    <td align="right">DESCRIPTION</td>
    <td>Allows to add, delete or check if a domain exists in<br/>
the local black list.</td>
  </tr>
  <tr>
    <td align="right">METHODS</td>
    <td>POST, GET, DELETE</td>
  </tr>
  <tr>
    <td align="right">URL</td>
    <td>bl/domain/&lt;string:domain></td>
  </tr>
  <tr>
    <td align="right">PARAMETERS</td>
    <td>None</td>
  </tr>
  <tr>
    <td align="right" valign="top">RETURNS</td>
    <td>HTTP/1.1 204 No Content
    </td>
  </tr>
</table>

The email black list specification is shown below: 
<table style="width:100%"> 
  <tr>
    <td align="right">DESCRIPTION</td>
    <td>Allows to add, delete or check if an email exists in<br/>
the local black list.</td>
  </tr>
  <tr>
    <td align="right">METHODS</td>
    <td>POST, GET, DELETE</td>
  </tr>
  <tr>
    <td align="right">URL</td>
    <td>bl/email/&lt;string:email></td>
  </tr>
  <tr>
    <td align="right">PARAMETERS</td>
    <td>None</td>
  </tr>
  <tr>
    <td align="right" valign="top">RETURNS</td>
    <td>HTTP/1.1 204 No Content
    </td>
  </tr>
</table>


### Email Risk Evaluation Service
This is the most important service of **Cartuxeira**. The email risk evaluation is relying on different black lists, machine learning techniques and third party services

The email risk evaluation specification is shown below:
<table style="width:100%"> 
  <tr>
    <td align="right">DESCRIPTION</td>
    <td>Evaluates the email risk relying on offline and online<br/> 
black lists, machine learning and third party services.</td>
  </tr>
  <tr>
    <td align="right">METHODS</td>
    <td>GET</td>
  </tr>
  <tr>
    <td align="right">URL</td>
    <td>risk/email/&lt;string:email></td>
  </tr>
  <tr>
    <td align="right">PARAMETERS</td>
    <td>None</td>
  </tr>
  <tr>
    <td align="right" valign="top">RETURNS</td>
    <td>HTTP/1.1 200 OK<pre>
{
  "risk_score": "Low",
  "domain": {
    "is_dga": false,
    "is_in_offline_blacklist": false,
    "is_in_online_blacklist": false
  },
  "email": {
    "is_ega": false,
    "is_in_offline_blacklist": false,
    "reputation": {
        "details": {
            "accept_all": false,
            "blacklisted": false,
            "credentials_leaked": true,
            "credentials_leaked_recent": false,
            "data_breach": true,
            "days_since_domain_creation": 11587,
            "deliverable": false,
            "disposable": false,
            "dmarc_enforced": true,
            "domain_exists": true,
            "domain_reputation": "high",
            "first_seen": "07/01/2008",
            "free_provider": false,
            "last_seen": "05/21/2022",
            "malicious_activity": false,
            "malicious_activity_recent": false,
            "new_domain": false,
            "primary_mx": "mx.example.org",
            "profiles": ["twitter"],
            "spam": false,
            "spf_strict": true,
            "spoofable": false,
            "suspicious_tld": false,
            "valid_mx": true
        },
        "references": 101,
        "reputation": "high",
        "summary": "Not suspicious.",
        "suspicious": false
      }
  }
}</pre>
    </td>
  </tr>
</table>


### Other REST API details
#### Version Prefix
All API routes are prefixed with `/v1/`.

**Backwards compatibility:** At the current version, **Cartuxeira** does not yet promise backwards compatibility even with the v1 prefix.

#### HTTP Status Codes
The following HTTP status codes are used throughout the API.
* `200` - Success with data.
* `204` - Success, no data returned.
* `400` - Invalid request, missing or invalid data.
* `404` - Invalid path or requested resource not found.
* `409` - Invalid request which generates a conflict with the current state of the target resource.
* `500` - Internal server error. An internal error has occurred, try again later. If the error persists, report a bug.
* `503` - Some **Cartuxeira** service is down. Review **Cartuxeira** logs.


## Bonus Track: Quick Start with Docker Compose

This section describes the installation of **Cartuxeira** using ```docker-compose```, including the Mongo database and the **Cartuxeira** server. 

Execute the following commands in the root folder of **Cartuxeira** and then, the **Cartuxeira** server will start listening at port 5000:

```bash
    docker-compose build
    docker-compose up -d
```

## Bugs and Feedback
For bugs, questions and discussions please use the [Github Issues](https://github.com/eliasgranderubio/cartuxeira/issues) or ping us on Twitter ([@3grander](https://twitter.com/3grander) or [@DLTorreLand](https://twitter.com/DLTorreLand)).