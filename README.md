# This project use removed version of SDIP 😢

# SDIP kzkgop/ZTM to REST api v2

SDIP KZKGOP/ZTM is tracking system for delays in city buses in Silesia (Without any public API).

This give you easy to REST API for your own personal use.

### Prerequisites
Runtime: 
```
Python 3 (python 3.8 recommended)
```
Requirements:
```
pip install -r requirements.txt
```

## Usage
This app runs as web server giving you few endpoints: 

* [List of lines](docs/list.md) : `GET /line/list`
* [List vehicles on line](docs/vehicles.md) : `POST /route/vehicles`
* [Current state of bus](docs/state.md) : `POST /vehicle/state`
* [Times of incoming stops](docs/journey.md) : `POST /vehicle/journey`

For resting purposes:
* [State](docs/state.md) and [journey](docs/journey.md) in one : `POST /vehicle/status`
* Does all requests while giving only line number : `POST /line/details`


## Authors

* [**Grzegorz M**](https://github.com/grzesjam) - *Creator* -

## License

This project is licensed under the **Mozilla Public License Version 2.0**
- see the [LICENSE](LICENSE) file for details
