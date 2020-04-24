# Snippet

import threading

# Run a script function in a separate thread
def run_bg(target_func, args):
  t = threading.Thread(target=target_func, args=args)
  t.start()

# End snippet