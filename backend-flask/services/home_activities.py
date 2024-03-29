from datetime import datetime, timedelta, timezone
from opentelemetry import trace

# Honeycomb - instantiate a tracer, the tracer provider was already instatiated in app.py
tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(logger,cognito_user_id=None):
    logger.info('Hello Cloudwatch! from home_activities /api/activities/home')
    logger.info(cognito_user_id)

    with tracer.start_as_current_span("home-activities-mock-data"):
      # span make sure span context is the correcnt span
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      span.set_attribute("app.test", "hello world")
    results = [{
      'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      'handle':  'Andrew Brown',
      'message': 'Cloud is very fun!',
      'created_at': (now - timedelta(days=2)).isoformat(),
      'expires_at': (now + timedelta(days=5)).isoformat(),
      'likes_count': 5,
      'replies_count': 1,
      'reposts_count': 0,
      'replies': [{
        'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
        'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Worf',
        'message': 'This post has no honor!',
        'likes_count': 0,
        'replies_count': 0,
        'reposts_count': 0,
        'created_at': (now - timedelta(days=2)).isoformat()
      }],
    },
    {
      'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
      'handle':  'Worf',
      'message': 'I am out of prune juice',
      'created_at': (now - timedelta(days=7)).isoformat(),
      'expires_at': (now + timedelta(days=9)).isoformat(),
      'likes': 0,
      'replies': []
    },
    {
      'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
      'handle':  'Garek',
      'message': 'My dear doctor, I am just simple tailor',
      'created_at': (now - timedelta(hours=1)).isoformat(),
      'expires_at': (now + timedelta(hours=12)).isoformat(),
      'likes': 0,
      'replies': []
    }
    ]
    if cognito_user_id != None:
      extra_crud = {
      'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
      'handle':  'Garek',
      'message': 'Extra Crud!!!!',
      'created_at': (now - timedelta(hours=1)).isoformat(),
      'expires_at': (now + timedelta(hours=12)).isoformat(),
      'likes': 0,
      'replies': []
      }
      results.insert(0,extra_crud)
    #with tracer.start_as_current_span("home-activities-mock-data"): if I uncomment this then it attributes make it into honeycomb but as another span, not within first span
    span = trace.get_current_span()
    span.set_attribute("app.result_length", len(results))
    span.set_attribute("app.tag", 'taggingtest')
    span.set_attribute("app.test2", 'goodbye world')
    return results
