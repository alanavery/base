{
    'standard, street view': {
        '1 king': [ < Room: 101 > , < Room: 105 > , < Room: 203 > , < Room: 207 > ],
        '2 queens': [ < Room: 103 > , < Room: 107 > , < Room: 201 > , < Room: 205 > ]
    },
    'standard, courtyard view': {
        '2 queens': [ < Room: 102 > , < Room: 106 > , < Room: 204 > , < Room: 208 > ],
        '1 king': [ < Room: 104 > , < Room: 108 > , < Room: 202 > , < Room: 206 > ]
    },
    'suite, street view': {
        '1 king': [ < Room: 109 > ],
        '2 queens': [ < Room: 209 > ]
    },
    'suite, courtyard view': {
        '2 queens': [ < Room: 110 > ],
        '1 king': [ < Room: 210 > ]
    }
}

  <ul>
    {% for bed_type in results.room_type %}
    <li>{{ bed_type }} <button>Book</button></li>
    {% endfor %}
  </ul>

<a href="/book/{{ bed }}"><button>Book</button></a>

http://127.0.0.1:8000/book/101