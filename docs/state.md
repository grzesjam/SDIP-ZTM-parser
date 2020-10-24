# Current state of bus

Used to get next stop, its delay, last stop and journey.

**URL** : `/vehicle/state`

**Method** : `POST`

**Data constraints**

```json
{
    "ID": "[Internal ID bus]"
}
```

**Data example**

```json
{
    "ID": "67"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "next": "Gliwice Plac Piastów",
  "delay": "Brak opóźnienia",
  "journey": "1391823",
  "last": "Katowice Mickiewicza"
}
```

## Note

- Internal ID of bus can be get from [/route/vehicles](/docs/vehicles.md)
- This endpoint can be used with GET using argument ID e.g. `/vehicle/state?ID=67`