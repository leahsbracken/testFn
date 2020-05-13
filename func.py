import io
import json

from fdk import response

directors_dict = ({"Psycho": "Alfred Hitchcock", "Batman": "Tim Burton", "Alien": "Ridley Scott", "Predator": "John McTiernan"})

def handler(ctx, data: io.BytesIO=None):
    movie = "Psycho"
    try:
        body = json.loads(data.getvalue())
        movie = body.get("movie")
    except (Exception, ValueError) as ex:
        print(str(ex))

    director = directors_dict[movie]
    response_data = {
    "movie": movie,
    "director"
    : director
    }

    return response.Response(
        ctx, response_data=json.dumps(
            response_data),
        headers={"Content-Type": "application/json"}
    )
