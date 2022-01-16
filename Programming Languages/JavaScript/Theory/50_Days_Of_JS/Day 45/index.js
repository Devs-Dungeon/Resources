function findOutlier(integers) {
  //your code here
  if(integers[0]%2 === 0)
    {
        if(integers[1]%2 !== 0)
        {
            if(integers[2]%2 !== 0)
              return integers[0];
            else
              return integers[1];  
        }
        else
        {
            for(let i=2;i<integers.length;i++)
              if(integers[i]%2 !== 0)
                  return integers[i];
        }  
    }
  
    if(integers[0]%2 !== 0)
    {
        if(integers[1]%2 === 0)
        {
            if(integers[2]%2 === 0)
              return integers[0];
            else
              return integers[1];  
        }
        else
        {
            for(let i=2;i<integers.length;i++)
              if(integers[i]%2 === 0)
                  return integers[i];
        }  
    }
}
