import org.scalatest.funsuite.AnyFunSuite
import org.scalamock.scalatest.MockFactory
import scala.concurrent.Future
import scala.concurrent.Await
import scala.concurrent.duration.*
import com.restfb.types.User

// https://www.baeldung.com/scala/scalamock
// https://www.scalatest.org/user_guide/testing_with_mock_objects

class FacebookSuite extends AnyFunSuite with MockFactory:
  test("compareLikes fetches all users successfully") {
    val mockClient = mock[FacebookClient]

    val user1 = new User()
    user1.setId("42")
    user1.setName("Włodzimierz")

    val user2 = new User()
    user2.setId("67")
    user2.setName("Bonifacy")

    (mockClient.getUser)
      .expects("42")
      .returning(Future.successful(user1))

    (mockClient.getUser)
      .expects("67")
      .returning(Future.successful(user2))

    val result = FacebookService.compareLikes(
      mockClient, "test.log", "42", "67"
    )

    Await.result(result, 5.seconds)
  }

  test("compareLikes handles failed Facebook API requests") {
    val mockClient = mock[FacebookClient]

    (mockClient.getUser)
      .expects("404")
      .returning(Future.failed(new RuntimeException("Facebook API error, URL: http://...")))

    val result = FacebookService.compareLikes(
      mockClient, "test.log", "404"
    )

    Await.result(result, 5.seconds)
  }
