{ pkgs ? import <nixpkgs> {} }:

pkgs.mkReplit {
  src = ./.;
  static = ./static;
}
