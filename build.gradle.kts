plugins {
    application
    kotlin("jvm") version "1.9.22" // or your kotlin version.
}

repositories {
    mavenCentral()
}

dependencies {
    implementation(kotlin("stdlib"))
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.10.2")
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine:5.10.2")
    implementation("org.projectlombok:lombok:1.18.36") // Use the latest version
    annotationProcessor("org.projectlombok:lombok:1.18.36") // Use the latest version
    testImplementation("org.projectlombok:lombok:1.18.36")
    testAnnotationProcessor("org.projectlombok:lombok:1.18.36")
}

application {
    mainClass.set("GameRunner") // set to the main class
}

tasks.test {
    useJUnitPlatform()
}

java {
    sourceCompatibility = JavaVersion.VERSION_21
    targetCompatibility = JavaVersion.VERSION_21
}