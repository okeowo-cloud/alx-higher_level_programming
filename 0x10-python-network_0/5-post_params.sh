#!/usr/bin/bash
# Post
# variable 'email' = 'test@gmail.com'
# variable 'subject' = 'I will always be here for PLD'
curl -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
