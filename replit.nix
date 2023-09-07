{ pkgs }: {
  deps = [
    pkgs.python39Packages.pip
    pkgs.qtile
    pkgs.python39Packages.flask
  ];
}