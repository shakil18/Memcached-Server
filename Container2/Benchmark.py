import os
import stat

def prepare_exp(SSHHost, SSHPort, REMOTEROOT, optpt):
    f = open("config", 'w')
    f.write("Host benchmark\n")
    f.write("   Hostname %s\n" % SSHHost)
    f.write("   Port %d\n" % SSHPort)
    f.close()

    f = open("run-experiment.sh", 'w')
    f.write("#!/bin/bash\n")
    f.write("set -x\n\n")

    #f.write("ssh -F config benchmark \"nohup ls dummy -p 11222 -P memcached.pid > memcached.out 2> memcached.err &\"\n") # adjust this line to properly start memcached

    f.write("sshpass -p \"screencast\" ssh -F config benchmark -o StrictHostKeyChecking=no -p 22 \"memcached -u root -p 11222 -P memcached.pid > memcached.out 2> memcached.err &\"\n")

   #f.write("RESULT=`ssh -F config benchmark \"pidof memcachd\"`\n")
   
    f.write("RESULT=`sshpass -p \"screencast\" ssh -F config benchmark -o StrictHostKeyChecking=no -p 22 \"pidof memcached\"`\n")

    f.write("sleep 5\n")

    f.write("if [[ -z \"${RESULT// }\" ]]; then echo \"memcached process not running\"; CODE=1; else CODE=0; fi\n")
        
    #f.write("%s/dummy --execute-number=%d --concurrency=%d -s %s > stats.log\n\n" % (REMOTEROOT, optpt["noRequests"], optpt["concurrency"], SSHHost)) #adjust this line to properly start the client
    
    f.write("mcperf --linger=0 --timeout=5 --num-conns=%d   --server=%s --port=11222 2> stats.log\n\n" % ( optpt["noRequests"],  SSHHost)) #adjust this line to properly start the client

    # add a few lines to extract the "Response rate" and "Response time \[ms\]: av and store them in $REQPERSEC and $LATENCY"
   
    f.write("REQPERSEC=$(cat stats.log | grep \"Response rate\" | awk '{print $3}')\n")
    f.write("LATENCY=$(cat stats.log | grep \"Response time \[ms\]: avg\" | awk '{print $5}')\n")
    f.write("echo \"${REQPERSEC} ${LATENCY}\"\n") 
   
    #f.write("sshpass -p \"screencast\" ssh -F config benchmark -o StrictHostKeyChecking=no -p 22 \"kill -9 $(pidof memcached)\"\n")

    f.write("echo \"requests latency\" > stats.csv\n")
    f.write("echo \"$REQPERSEC $LATENCY\" >> stats.csv\n")
    
    #f.write(" scp -F config benchmark:~/memcached.* .\n")

    f.write("if [[ $(wc -l <stats.csv) -le 1 ]]; then CODE=1; fi\n\n")
    
    f.write("exit $CODE\n")

    f.close()
    
    os.chmod("run-experiment.sh", stat.S_IRWXU) 
