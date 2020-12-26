def invokeMethod1():
    import time
    directory1 = 'C:/python-' + \
        time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    import os
    isExists=os.path.exists(directory1)
    if not isExists:
        print(directory1 + " Not Exists")
        os.makedirs(directory1) 
    else:
        print(directory1 + " Exists")
    import logging
    logging.basicConfig(filename=directory1 + '/test.log',
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s'
                        )
    logging.info('invoke method!')

if __name__ == '__main__':
    invokeMethod1()
