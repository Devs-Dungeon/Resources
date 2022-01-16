# Categorize New Member

## Instructions
- The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.
- To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

## Input
- Input will consist of a array of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

## Output
- Output will consist of a list of string values stating whether the respective member is to be placed in the senior or open category.

## Example
- (openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]) returns ['Open', 'Senior', 'Open', 'Senior']

## Challenges (0/2 done)
- [ ] openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]) should return ['Open', 'Senior', 'Open', 'Senior']
- [ ] openOrSenior([[3, 12],[55,1],[91, -2],[53, 23]]) should return['Open', 'Open', 'Open', 'Open']
- [ ] openOrSenior([[59, 12],[55,-1],[12, -2],[12, 12]]) should return ['Senior', 'Open', 'Open', 'Open'])

```js
function openOrSenior(data) {
  // your code goes below
}

let output = openOrSenior([
  [45, 12],
  [55, 21],
  [19, -2],
  [104, 20],
]);

console.log(output);
```
