function isTriangle(a, b, c) {
  // your code here
  return ((a>0 && b>0 && c>0) && (((a+b)>c) && ((b+c)>a) && ((a+c)>b)));
}
