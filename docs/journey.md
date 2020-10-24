# Current state of bus

Used to get last bus stop and all incoming bus stops with there time or arrival and time remaining.

**URL** : `/vehicle/journey`

**Method** : `POST`

**Data constraints**

```json
{
    "ID": "[ID of journey]"
}
```

**Data example**

```json
{
    "ID": "1391823"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "last": "Katowice Mickiewicza",
  "stops": [
    {
      "name": "Katowice Chorzowska",
      "time": "19:57",
      "inTime": "1 minut"
    },
    {
      "name": "Katowice Aleja Korfantego",
      "time": "19:59",
      "inTime": "3 minut"
    }
  ]
}
```

## Note

- ID of journey can be get from [/vehicle/state](/docs/state.md)
- This endpoint can be used with GET using argument ID e.g. `/vehicle/journey?ID=1391823`