# Clean Assist


This is a simple library to help data scientists observe how to clean their data.

### Copy paste the following lines of code:


diff --git a/foo.c b/foo.c
index 30cfd169..8de130c2 100644
--- a/foo.c
+++ b/foo.c
@@ -1,5 +1,5 @@
 #include <string.h>

 int check (char *string) {
-    return !strcmp(string, "ok");
+    return (string != NULL) && !strcmp(string, "ok");
 }

```diff
+ <br>this text is highlighted in green
```


