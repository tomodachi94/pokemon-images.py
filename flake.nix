# SPDX-FileCopyrightText: 2024 Tomodachi94 and contributors
#
# SPDX-License-Identifier: MIT

{
  description = "A Nix-flake-based Python development environment";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = { self, nixpkgs }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      devShells = forEachSupportedSystem ({ pkgs }: {
        default = pkgs.mkShellNoCC {
          packages = with pkgs; [
		    python3
            poetry
            ruff
			just
            python3Packages.mypy
			reuse
          ];
        };
      });
    };
}
