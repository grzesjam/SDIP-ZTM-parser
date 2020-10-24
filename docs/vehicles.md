# List vehicles on line

Used to get all busses currently on road.

**URL** : `/route/vehicles`

**Method** : `POST`

**Data constraints**

```json
{
    "ID": "[Intenal ID of line]"
}
```

**Data example**

```json
{
    "ID": "13"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
[67, 39, 7]
```


## Note

This endpoint can be used with GET using argument ID e.g. `/route/vehicles?ID=13`