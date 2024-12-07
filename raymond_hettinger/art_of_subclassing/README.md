# The Art of Sub-classing
> Author: Raymond Hettinger
> 
> Written by: Vinay Kumar

## Pattern of Sub-classing

### `Framework` pattern

> As mentioned in GoF design-patterns book.

1. The parent class supplies all the **"controller"** functionality and makes calls to pre-named **stub** methods.
2. The subclass overrides **stub** methods of interest.
3. For example, `SimpleHTTPServer` runs an event loop and dispatches HTTP requests to stub methods like `do_HEAD()` and `do_GET()`.

> Someone writing an `HTTP` server would use a subclass (of `SimpleHTTPServer` class) to supply the desired actions in the event of a `GET` or `HEAD` request.

> Try NOT to USE Framework pattern.

### `Dynamic Dispatch` pattern

> Dynamic Dispatch to subclass methods.

1. The _parent_ class uses `getattr()` to dispatch a new functionality.
2. The _child_ class **implements** appropriately named methods.
3. Example from `cmd.py`:
   ```python
    def onecmd(self, cmd, arg):
        try:
            func = getattr(self, "do_" + cmd)
        except AttributeError:
            return self.default(cmd)
        return func(arg)
   ```
4. How it might be used in a subclass:
   ```python
   def do_pendown(self):
        self.canvas.setpen(1)
    ```

> Try to USE Dynamic Dispatch pattern

## Call patterns for sub-classing

