# Hanime

The **Hanime Python Library** allows you to interact with Hanime's API, providing functionalities to fetch information about videos, images, channels, and perform searches. This library is designed to be user-friendly, offering a variety of features for building applications or tools that utilize Hanime's data.

## Requirements

Before using this library, ensure you have the following requirements installed:

- Python 3.6 or later
- Requests library (`pip install requests`)
- Beautiful Soup library (`pip install beautifulsoup4`)

## Table of Contents

1. [HanimeUser Class](#hanimeuser-class)
2. [UserClient Class](#userclient-class)
3. [ImageClient Class](#imageclient-class)
4. [SearchPayload Data Class](#searchpayload-data-class)
5. [BaseSearchHeaders Data Class](#basesearchheaders-data-class)
6. [ParsedData Class](#parseddata-class)
7. [SearchClient Class](#searchclient-class)
8. [HanimeVideo Class](#hanimevideo-class)
9. [Credits](#credits)

---

## HanimeUser Class

**HanimeUser** is a class representing a user's information from Hanime. It is initialized with user data and provides a dynamic way to access user attributes.

### `__init__(self, data)`

- `data` (dict): User data containing various attributes.

Example:

```python
user_data = {"username": "example_user", "id": 12345, "avatar_url": "https://example.com/avatar.jpg"}
hanime_user = HanimeUser(user_data)
username = hanime_user.username
```

## UserClient Class

**UserClient** interacts with Hanime's user-related API endpoints, providing methods for fetching user-related information.

### `BASE_URL` Class Attribute

- `BASE_URL` (str): The base URL for Hanime's API.

### `__init__(self, cookies={'in_d4': '1', 'in_m4': '1'}, headers={})`

- `cookies` (dict): Custom cookies to include in requests.
- `headers` (dict): Custom HTTP headers to include in requests.

Example:

```python
user_client = UserClient() # Leave cookies & headers as none, therefore the library can use the correct ones. Unless you have fresh ones, that work maybe with `x-signature`.
```

### `create_default_headers()`

This method returns a dictionary of default HTTP headers for making requests to Hanime's API.

Example:

```python
default_headers = UserClient.create_default_headers()
```

### `get_channel_info(channel_id)`

This method retrieves information about a Hanime channel based on the provided channel ID.

- `channel_id` (int): The ID of the channel to fetch information for.

Example:

```python
channel_info = user_client.get_channel_info('test-123')
```

The returned value is a **HanimeUser** object representing the channel's information. In case of an error, the method will return None.

## ImageClient Class

**ImageClient** provides methods for interacting with Hanime's community image uploads, including utility methods for building requests and parsing responses.

### `create_default_headers()`

This method returns a dictionary of default HTTP headers for making requests to Hanime's API.

Example:

```python
headers = ImageClient.create_default_headers()
```

### `build_query(channel_names: List[str], offset: int)`

This method builds a query dictionary for fetching community uploads based on channel names and an offset value.

- `channel_names` (List[str]): A list of channel names to filter the uploads.
- `offset` (int): The offset value for pagination.

Example:

```python
query = ImageClient.build_query(['channel1', 'channel2'], 10)
```

### `parse_community_uploads(data: dict)`

This method parses the data returned from a Hanime API response and returns a list of **HanimeImage** objects.

- `data` (dict): The API response data.

Example:

```python
data = {"data": [...] }  # API response data
images = ImageClient.parse_community_uploads(data)
```

### `get_community_uploads(channel_names: List[str], offset: int)`

This method makes an HTTP GET request to fetch community uploads based on channel names and an offset value.

- `channel_names` (List[str]): A list of channel names to filter the uploads.
- `offset` (int): The offset value for pagination.

Example:

```python
images_data = ImageClient.get_community_uploads(['channel1', 'channel2'], 10)
```

## SearchPayload Data Class

**SearchPayload** is a data class representing a payload for searching on Hanime. It includes attributes for search text, tags, brands, ordering, and pagination.

### `create_default_payload()`

This method creates a default payload with default values for searching.

Example:

```python
default_payload = SearchPayload.create_default_payload()
```

### `convert_ordering(ordering)`

This method converts an ordering option into the corresponding value used in the payload.

Example:

```python
ordering_value = SearchPayload.convert_ordering('recent_uploads')
```

### `convert_order_by(order_by)`

This method converts an order-by option into the corresponding value used in the payload.

Example:

```python
order_by_value = SearchPayload.convert_order_by('most_views')
```

## BaseSearchHeaders Data Class

**BaseSearchHeaders** is a data class representing HTTP headers for making search requests. It includes attributes for common HTTP headers.

### `create_default_headers()`

This method creates a default set of HTTP headers for making search requests.

Example:

```python
default_headers = BaseSearchHeaders.create_default_headers()
```

## ParsedData Class

**ParsedData** is a class used to parse and work with data returned in search responses. It provides a way to access attributes in a dictionary-like manner and parse HTML descriptions.

Example:

```python
parsed_data = ParsedData(data)
description = parsed_data.description
```

## SearchClient Class

**SearchClient** allows you to interact with Hanime's search functionality, providing methods for searching, filtering responses, and parsing hits data.

### `__init__(client_identifier=None)`

This method initializes a **SearchClient** with an optional client identifier.

Example:

```python
search_client = SearchClient(client_identifier='my-client')
```

### `search(payload)`

This method sends a search request using the provided payload and returns the JSON response.

Example:

```python
search_payload = SearchPayload(search_text='hentai', tags=['tag1', 'tag2'])
response = search_client.search(search_payload)
```

### `filter_response(base_response, filter_options)`

This static method filters the response data based on specified filter options.

Example:

```python
filtered_response = SearchClient.filter_response(base_response, ['hits', 'total'])
```

### `parse_hits_data(response)`

This static method parses hits data from the response and returns a list of **ParsedData** objects.

Example:

```python
hits_data = SearchClient.parse_hits_data(response)
```

## HanimeVideo Class

**HanimeVideo** is a class used to represent information about a video on Hanime. It is initialized with video data and provides a dynamic way to access video attributes.

### `__init__(self, data)` Method

- `data` (dict): Video data containing various attributes.

Example:

```python
video_data = {"title": "Example Video", "duration": 1200, "tags": ["tag1", "tag2"]}
hanime_video = HanimeVideo(video_data)
title = hanime_video.title
```

### `__getattr__(self, name)`

This method allows dynamic access to video attributes. It returns the value of the requested attribute if it exists in the video data.

Example:

```python
duration = hanime_video.duration
```

### `description` Property

This property parses and returns the description of the video from the HTML description provided in the data.

Example:

```python
description = hanime_video.description
```

## VideoClient Class

**VideoClient** interacts with Hanime's video-related API endpoints, providing methods for fetching video information and random videos based on tags.

### `BASE_URL` Class Attribute

- `BASE_URL` (str): The base URL for Hanime's API.

### `TAGS` Class Attribute

- `TAGS` (List[str]): A list of valid tags used for filtering videos.

### `__init__(self, cookies={'in_d4': '1', 'in_m4': '1',}, client_identifier=None)`

- `cookies` (dict): Custom cookies to include in requests.
- `client_identifier` (str): An optional client identifier used in headers.

Example:

```python
video_client = VideoClient(client_identifier='my-client')
```

### `create_default_headers(client_identifier: str = None)`

This method returns a dictionary of default HTTP headers for making requests to Hanime's API. It allows you to include a client identifier in the headers.

Example:

```python
default_headers = VideoClient.create_default_headers(client_identifier='my-client')
```

### `get_video_info(video_id)`

This method retrieves information about a Hanime video based on the provided video ID.

- `video_id` (int): The ID of the video to fetch information for.

Example:

```python
video_info = video_client.get_video_info(123)
```

The returned value is a **HanimeVideo** object representing the video's information. In case of an error, the method will return None.

### `get_random_video()`

This method fetches a random Hanime video.

Example:

```python
random_video = video_client.get_random_video()
```

The returned value is a **HanimeVideo** object representing the random video. In case of an error, the method will return None.

### `get_random_video_tag(num_tags: int = 1, include_tags: Optional[List[str]] = None, exclude_tags: Optional[List[str]] = None)`

This method fetches a random Hanime video based on specified tags.

- `num_tags` (int): The number of tags to include in the search.
- `include_tags` (Optional[List[str]]): A list of tags to include in the search.
- `exclude_tags` (Optional[List[str]]): A list of tags to exclude from the search.

Example:

```python
random_video = video_client.get_random_video_tag(num_tags=3, include_tags=['tag1', 'tag2'])
```

The method returns a list of **ParsedData** objects representing the search results based on the specified tags. In case of an error, the method will raise **InvalidTagsError** if invalid tags are provided or raise a **ValueError** if there are not enough valid tags available after filtering.

## Credits

- **Author**: alluding
- **Discord**: puud
- **Email**: bio@fbi.ac

## Author Note

I created this library out of sheer boredom. While it's not my top priority, I won't abandon the project. If there are issues that need fixing, I'll address them. I'll also work on new features if the need arises. Contributions are welcome through issues or pull requests.

Feel free to contact the author (me) for any queries or contributions.
