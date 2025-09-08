{
  inputs = {
    utils.url = "github:numtide/flake-utils";
  };
  outputs = {
    self,
    nixpkgs,
    utils,
  }:
    utils.lib.eachDefaultSystem (
      system: let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            lolcat
            (
              python313.withPackages
              (
                ppkgs:
                  with ppkgs; [
                    ipython
                    ipykernel
                    jupyter-all
                    jupyterlab
                    pandas
                    numpy
                    joblib
                    matplotlib
                    scikit-learn
                    pytest
                    mypy
                    tqdm
                  ]
              )
            )
          ];
        };
      }
    );
}
