#! /usr/bin/env bash

: <<'END'
Author:   Christopher Smiga
e-Mail:   CSmiga@yahoo.com
LinkedIn: https://www.linkedin.com/in/csmiga/

File:    nfunct.sh
END

declare CONFIG=$HOME/Projects/nfunct/conf/nfunct.conf
#declare CONFIG=$HOME/Projects/nfunct_behaviors/plutotv/conf/plutotv.conf
declare BIN=/root/Projects/venv3/bin/locust
declare PROCESS=$(pgrep locust)

function nfunct_start () {
    if [ -z "$PROCESS" ]
    then
        local OPTION=$(grep -Ev "^$|#" "$CONFIG" | \
            awk -F\, '{print $2 "--" $1}' | awk 'ORS=" "')
        # Debug "nfunct start" using output.
        #$BIN $OPTION
        # Process monitorng using "nfunct status".
        $BIN $OPTION 2> /dev/null &
        local PID=$(pgrep locust)
        echo "nfunct [ PID: $PID ] starting "
        sleep 1
        if [ -n "$PID" ]
        then
            echo "nfunct [ PID: $PID ] started "
        else
            echo "nfunct [ PID: None ] not running "
        fi
    else
        echo "nfunct [ PID: $PROCESS ] running "
    fi
}

function nfunct_status () {
    if [ -n "$PROCESS" ]
    then
        echo "nfunct [ PID: $PROCESS ] running "
    else
        echo "nfunct [ PID: None ] not running "
    fi                       
}

function nfunct_stop () {
    if [ -n "$PROCESS" ]
    then
        echo "nfunct [ PID: $PROCESS ] stopping"
        kill -SIGTERM "$PROCESS"
        sleep 1
        local PID=$(pgrep locust)
        if [ -z "$PID" ]
        then
            echo "nfunct [ PID: None ] stopped"
        else
            echo "nfunct [ PID: $PID ] running "
        fi
    else
        echo "nfunct [ PID: None ] not running "
    fi
}

case "$1" in
    help)
        echo
        echo "Binary: $($BIN --version)"
        echo "Config: $(echo $CONFIG)"
        echo
        echo "Reading config file..."
        echo
        cat $CONFIG
        ;;
    list)
        $BIN --list --locustfile $(awk '/^locustfile/ {print $2}' $CONFIG)
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
        $BIN --version
        ;;
    *)
        echo "Usage: $0 {start|stop|status|list|version|help}"
        exit 1
esac

exit 0
