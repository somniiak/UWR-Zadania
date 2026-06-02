import scala.concurrent.Await
import scala.concurrent.duration.*

/*
Guide on how to get AppSecret and AccessToken (because it's bizarre how hard it is):

1. Go to https://developers.facebook.com/ and create a new app with use case:
  "Authenticate and request data from users with Facebook Login" (??)

2. Customze use case -> turn `user_likes` on

3. Get AppSecret:
  Apps -> APP_NAME -> App settings -> Basic -> App Secret

4. Get AccessToken:
  Go to https://developers.facebook.com/tools/explorer ->
  Add a permission -> User data permissions -> user_likes ->
  Generate Access Token
*/

@main def main(): Unit =
  val logFile: String = "likes.log"
  val client: FacebookClient = FacebookAdapter

  Await.result(
    FacebookService.compareLikes(client, logFile, "me", "1", "me", "me"),
    30.seconds
  )
