{
  description = "Development shell for guardianproject.info";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { nixpkgs, ... }:
    let
      systems = [
        "x86_64-linux"
        "aarch64-linux"
      ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
    in
    {
      devShells = forAllSystems (system:
        let
          pkgs = import nixpkgs { inherit system; };
          pythonPath = pkgs.python3.pkgs.makePythonPath (
            [ pkgs.fdroidserver ] ++ pkgs.fdroidserver.propagatedBuildInputs
          );
        in
        {
          default = pkgs.mkShell {
            packages = with pkgs; [
              curl
              fdroidserver
              git
              gnupg
              go
              gnumake
              hugo
              mawk
              nodejs
              python3
              sassc
              unzip
              wget
            ];

            shellHook = ''
              export PYTHONPATH="${pythonPath}:$PYTHONPATH"
              export GPG_WKS_CLIENT="${pkgs.gnupg}/bin/gpg-wks-client"
            '';
          };
        });
    };
}
