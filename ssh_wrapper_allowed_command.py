dallow={ 'root@zulu': ['svcadm enable dnrd'
                       ,'svcadm disable dnrd'
                       ,'scp -t /usr/local/etc/dnrd/master'
                       ,'scp -t -- qw'
                       ,'ls']
       }

if '__main__'==__name__:
    import sys
    sys.exit()
