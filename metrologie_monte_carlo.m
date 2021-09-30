close all; clear all; clc; 

%Definir les grandeurs d' entree X (MATRICE) 
%Definir les incertitudes types u(X)
%Definir la fonction Y=f(x) = x1 + x2
%Calculer N valeurs de Y -> y=(1,N)
%Calcul de moyenne de y et de uY= std(yi)
%Calculer les facteurs de sensibilites

%Representer les resultats sous forme d'histogramme fct hist

%%% DEFINITION DES PARAMETRES

N = input('entrez la valeur de N =  ');;

X1 = input('entrez la valeur de X1 =  ');
X2 = input('entrez la valeur de X2 =  ');;

uX1 = input('entrez la valeur de uX1 =  ');;
uX2 = input('entrez la valeur de uX2 =  ');;

X(1,:) = randn(1,N)*uX1 + X1;
X(2,:) = randn(1,N)*uX2 + X2 ;

%%% Trace des histogrammes
figure 1
hist(X(1,:),100)
title('Fonction de repartition des X1');
xlabel('Valeur de X');
ylabel("Nombre d' occurences");

figure 2
hist(X(2,:),100)
title('Fonction de repartition des X2');
xlabel('Valeur de X');
ylabel("Nombre d' occurences");


%%% Fonction etudiee

Y = X(1,:)+X(2,:);

figure 3
hist(Y,100);
title('Fonction de repartition de Y(X1,X2)');
xlabel('Valeur de Y');
ylabel("Nombre d' occurences");

moy_Y = sum(Y)/N ; 
uY = std(Y) ; 

disp("La valeur de la moyenne des Y est : "); 
disp(moy_Y);
disp("L'incertitude des Y est : ");
disp(uY);

%%% Facteurs de sensibilite derivees partielles selon x1 et x2

%% Avec X1 fixe 

X1_fixe = ones(1,N)*X1;
Y_X1_fixe = X1_fixe+X(2,:);
uY_X2 = std(Y_X1_fixe);

disp("L'incertitude uY(X2) est : ");
disp(uY_X2);

%% Avec X2 fixe

X2_fixe = ones(1,N)*X2 ;
Y_X2_fixe = X(1,:)+X2_fixe;
uY_X1 = std(Y_X2_fixe);

disp("L'incertitude uY(X1) est : ");
disp(uY_X1);

%% VÃ©rification de l'Ã©galitÃ© des carrÃ©s

disp("L'incertitude uY**2 vaut : ");
disp(uY**2);
disp("L'incertitude uY(X1)**2 + uY(X2)**2 vaut : ");
disp(uY_X2**2 + uY_X1**2);

disp("Ils sont egaux en theorie pour N tend vers l'infini, pour N grand la difference est faible");

%% Affichage des facteurs de sensibilitÃ©

figure 4

bar([uY,uY_X2,uY_X1]);
str = {'uY(X1,X2)';'uY(X2)';'uY(X1)'};
set(gca,'XTickLabel',str,'XTick',1:numel(str));
