# risk-calculator

## Development setup

## Deployment

If you need to work in the project, add features or edit content, you have to run the services separately.

- POSTGRESQL
  Depends if you use service
  ```
  service postgresql start
  ```
  or systemctl
  ```
  systemctl start postgresql
  ```
  in Ubuntu
- VueJS fronted

  ```
  yarn serve
  ```

Otherwise, you can deploy all the project by running a docker

```
docker-compose up --build
```

### CONSIDERATIONS

The charged model must be saved with the same scikit learn version of the repository
