# Icinga2 checks

## checks

---
* check_gitlab_api.py
* check_iostats.py


---
1. check_gitlab_api.py      
      -t token *token to read the api.*      
      -u url *url of the gitlab instanec. URL should end with a '/'*

2. check_iostats.py
    Doesn't need commandline paramaters

---


## example config
### example commands

```
object CheckCommand "iostatcheck"{
    import "plugin-check-command"
    command = ["check_iostat.py"]
}      
```

### example 

```
apply Service "iostatscheck"{
    import "generic-service"
    check_command = "iostatcheck"
    retry_interval = 30s
    command_endpoint = host.vars.client_endpoint
}
```