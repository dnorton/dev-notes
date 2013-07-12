# .bashrc

# User specific aliases and functions

## These variables should be set according to your local environment
PATH=$PATH:${HOME}/scripts
GLASSFISH_HOME=/glassfish #change me
CONF_DIR=/conf #change me


function _asadmin() { sudo -u tcuser ${GLASSFISH_HOME}/bin/asadmin --user admin --passwordfile ${CONF_DIR}/glassfish_password.txt $@; }
export _asadmin

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi
