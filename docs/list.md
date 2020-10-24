# List of lines

Provides list of line numbers and IDs of them.

**URL** : `/route/vehicles`

**Method** : `GET`

## Success Response

**Code** : `200 OK`

**Content examples**

There are two lines:
- line `0` with internal id `55` 
- line `1` with internal id `202`

```json
[
  {
    "name": "0",
    "id": "55"
  },
  {
    "name": "1",
    "id": "202"
  }
]
```