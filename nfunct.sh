#! /usr/bin/env bash

: <<'END'
Author:  Christopher Smiga
e-Mail:  CSmiga@Yahoo.com
ICQ:     5035779

File:    nfunct.sh
END

declare NFUNCT_BIN
declare NFUNCT_PROC
NFUNCT_BIN=/root/Projects/venv3/bin/locust
NFUNCT_PROC=$(pgrep locust)

function nfunct_start () {
    if [ -z "$NFUNCT_PROC" ]
    then
        local NFUNCT_HOME
        local NFUNCT_CFG
        local NFUNCT_ARG
        local NFUNCT_PID
        NFUNCT_HOME=$HOME/Projects/nfunct
        NFUNCT_CFG=$NFUNCT_HOME/conf/nfunct.conf
        NFUNCT_ARG=$(grep -Ev "^$|#" "$NFUNCT_CFG" | \
            awk -F\, '{print $2 "--" $1}' | awk 'ORS=" "')
        #$NFUNCT_BIN $NFUNCT_ARG
        $NFUNCT_BIN $NFUNCT_ARG 2> /dev/null &
        NFUNCT_PID=$(pgrep locust)
        echo "nfunct [ PID: $NFUNCT_PID ] starting "
        sleep 1
        if [ -n "$NFUNCT_PID" ]
        then
            echo "nfunct [ PID: $NFUNCT_PID ] started "
        else
            echo "nfunct [ PID: None ] not running "
        fi
    else
        echo "nfunct [ PID: $NFUNCT_PROC ] running "
    fi
}

function nfunct_status () {
    if [ -n "$NFUNCT_PROC" ]
    then
        echo "nfunct [ PID: $NFUNCT_PROC ] running "
    else
        echo "nfunct [ PID: None ] not running "
    fi                       
}

function nfunct_stop () {
    if [ -n "$NFUNCT_PROC" ]
    then
        echo "nfunct [ PID: $NFUNCT_PROC ] stopping"
        kill -SIGTERM "$NFUNCT_PROC"
        sleep 1
        local NFUNCT_PID
        NFUNCT_PID=$(pgrep locust)
        if [ -z "$NFUNCT_PID" ]
        then
            echo "nfunct [ PID: None ] stopped"
        else
            echo "nfunct [ PID: $NFUNCT_PID ] running "
        fi
    else
        echo "nfunct [ PID: None ] not running "
    fi
}

case "$1" in
    list)
        $NFUNCT_BIN --list --locustfile lib/testfile.py
        ;;
    start)
        nfunct_start
        ;;
    stop)
        nfunct_stop
        ;;
    status)
        nfunct_status
        ;;
    version)
        $NFUNCT_BIN --version
        ;;

    *)
        echo $"Usage: $0 {start|stop|status|list|version}"
        exit 1
esac

exit 0
