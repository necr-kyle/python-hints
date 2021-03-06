# print exception info in try-except
import traceback
try:
    print(1/0)
except Exception as e:
    print("##############################")
    print('str(Exception):\t', str(Exception))
    print('str(e):\t\t', str(e))
    print('repr(e):\t', repr(e))
    print('traceback.print_exc():', traceback.print_exc())
    print('traceback.format_exc():\n%s' % traceback.format_exc())
    print("##############################")
