#!/bin/bash

ansible all -m shell -a "sudo shutdown now" -i inventory
