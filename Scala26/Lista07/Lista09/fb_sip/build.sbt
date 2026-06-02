val scala3Version = "3.8.3"

lazy val root = project
  .in(file("."))
  .settings(
    name := "FB_SiP",
    version := "0.1.0-SNAPSHOT",

    scalaVersion := scala3Version,

    libraryDependencies += "org.scalameta" %% "munit" % "1.3.0" % Test,
    libraryDependencies += "io.github.cdimascio" % "dotenv-java" % "3.2.0",
    libraryDependencies += "com.restfb" % "restfb" % "2026.6.0",
    libraryDependencies += "com.lihaoyi" %% "os-lib" % "0.11.8",
    libraryDependencies += "org.scalamock" %% "scalamock" % "7.5.5" % Test,
    libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.20" % Test
  )
