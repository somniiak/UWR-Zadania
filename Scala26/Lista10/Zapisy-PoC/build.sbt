name := """zapisy-poc"""
organization := "org"

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayScala)

scalaVersion := "3.8.3"

libraryDependencies += guice
