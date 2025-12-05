package com.example.util;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.stream.Collectors;

public class BuildHelper {
  public static void main(String[] args) throws IOException {
    String outDir = args.length > 0 ? args[0] : "target/classes";
    Path base = Paths.get(outDir);
    if (!Files.exists(base)) {
      System.err.println("Output directory not found: " +
                         base.toAbsolutePath());
      return;
    }
    String content =
        Files.walk(base)
            .filter(p -> p.toString().endsWith(".class"))
            // use full path to the .class file because ckjm_ext reads files
            .map(p -> p.toString())
            // remove inner class files (keep only top-level .class)
            .filter(s -> !s.contains("$"))
            .distinct()
            .sorted()
            .collect(Collectors.joining(System.lineSeparator()));
    Path out = Paths.get("classlist.txt");
    Files.writeString(out, content);
    System.out.println("Wrote " + out.toAbsolutePath());
  }
}
