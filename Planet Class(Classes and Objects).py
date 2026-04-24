class Planet:
    def __init__(self, name, planet_type,star):
        self.name = name
        self.planet_type = planet_type
        self.star = star

        for attr in (name, planet_type, star):
            if not isinstance(attr, str):
                raise TypeError('name, planet type, and star must be strings' )
            if attr == '':
                raise ValueError('name, planet_type, and star must be non-empty strings')

    def orbit(self):
        return (f'{self.name} is orbiting around {self.star}...')

    def __str__(self):
        return (f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}')

planet_1 = Planet('Earth', 'Rock', 'Sol')
planet_2 = Planet('Mars', 'Rock', 'Sol')
planet_3 = Planet('Neptune', 'Gas Giant', 'Sol')

print(planet_1)
print(planet_2)
print(planet_3)
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())