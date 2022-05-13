from cloud import OwnCloud
import os

def main():
    oc = OwnCloud();

    #download dataset
    dataset_path = '/TechChallenge/Dataset/example.txt'
    success = oc.get_file(dataset_path)
    print("Success!" if success else "Fail to download dataset")

    #download model


    #train
    

if __name__ == "__main__":
    main()