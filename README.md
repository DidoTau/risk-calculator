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

Otherwise, you can deploy all the project by running:

```
./create_database.sh risk_calculator_db risk_calculator_user 1234
```

To create the database in the local environtment. The arguments to run the script mush be the same that the env. variables
on the backend docker service in docker-compose.yml.

Finally you execute:

```
docker-compose up --build
```

### CONSIDERATIONS

The charged model must be saved with the same scikit learn version of the repository
