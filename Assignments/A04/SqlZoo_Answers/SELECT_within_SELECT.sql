SELECT name FROM world WHERE population > (SELECT population FROM world WHERE name='Russia');

SELECT name FROM world WHERE gdp/population > (SELECT gdp/population FROM world WHERE name = 'United Kingdom') AND continent = 'Europe';

SELECT name,continent FROM world WHERE continent = (SELECT continent FROM world WHERE name = 'Argentina ') OR continent = (SELECT continent FROM world WHERE name = 'Australia') ORDER BY name;

SELECT name,population FROM world WHERE population > (SELECT population FROM world WHERE name = 'Canada') AND population < (SELECT population FROM world WHERE name = 'Poland');

SELECT name, CONCAT(ROUND(population/(SELECT population FROM world WHERE name = 'Germany')* 100),'%')  AS percentage FROM world WHERE continent = 'Europe';

SELECT name FROM world WHERE gdp > ALL(SELECT gdp FROM world WHERE continent = 'Europe' AND gdp IS NOT null);

SELECT continent, name, area FROM world x WHERE area >= ALL (SELECT area FROM world y WHERE y.continent=x.continent AND area>0);

SELECT continent, name FROM world x WHERE name <= ALL(SELECT name FROM world y WHERE x.continent = y.continent);

SELECT name, continent, population FROM world x WHERE 25000000 >= ALL(SELECT population FROM world y WHERE x.continent = y.continent);

SELECT name, continent FROM world x WHERE population > ALL(SELECT population * 3 FROM world y WHERE x.continent = y.continent AND x.name != y.name);