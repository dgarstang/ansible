# ansible

# Deploying

Deploy ansible code with the command:
```bash
ansible-playbook -i inventory --extra-vars "@../ansible-secrets/secrets" site.yaml
```
